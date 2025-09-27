
from device import Device
from device_manage import DeviceManager
from schedule import ScheduleManager
from fan import fan
from light import Light
from ac import ac
from washing_mac import WashingMachine

def main():
	device_manager = DeviceManager()
	schedule_manager = ScheduleManager()

	import datetime
	while True:
		# Schedule execution: check and update device status
		current_time = datetime.datetime.now().strftime('%H:%M')
		for s in schedule_manager.schedules:
			device_name = getattr(s, 'device', None)
			for d in device_manager.devices:
				if d.name == device_name:
					if s.is_active(current_time):
						d.turn_on()
					else:
						d.turn_off()
		print("\nSmart Home Menu")
		print("1. Add Device")
		print("2. List All Devices")
		print("3. Get Device Status")
		print("4. Control Device (ON/OFF)")
		print("5. Create Device Schedule")
		print("6. Manage Device Schedule")
		print("7. View All Schedules")
		print("8. Exit")
		choice = input("Enter your choice: ")

		if choice == '1':
			print("Select device type:")
			print("1. Fan")
			print("2. Light")
			print("3. AC")
			print("4. Washing Machine")
			print("5. Generic Device")
			dtype = input("Enter choice: ")
			name = input("Enter device name: ")
			if dtype == '1':
				new_device = fan(name)
			elif dtype == '2':
				new_device = Light(name)
			elif dtype == '3':
				new_device = ac(name)
			elif dtype == '4':
				new_device = WashingMachine(name)
			else:
				new_device = Device(name)
			device_manager.add_device(new_device)
			print(f"Device '{name}' added.")

		elif choice == '2':
			device_manager.view_devices()

		elif choice == '3':
			name = input("Enter device name: ")
			found = False
			for d in device_manager.devices:
				if d.name == name:
					print(d.get_status())
					found = True
			if not found:
				print("Device not found.")

		elif choice == '4':
			name = input("Enter device name: ")
			found = False
			for d in device_manager.devices:
				if d.name == name:
					found = True
					print("Control Options:")
					print("1. Turn ON")
					print("2. Turn OFF")
					if isinstance(d, fan):
						print("3. Set Speed")
					if isinstance(d, Light):
						print("4. Set Brightness")
					if isinstance(d, ac):
						print("5. Set Temperature")
					if isinstance(d, WashingMachine):
						print("6. Set Mode")
					ctrl = input("Enter option: ")
					if ctrl == '1':
						d.turn_on()
					elif ctrl == '2':
						d.turn_off()
					elif ctrl == '3' and isinstance(d, fan):
						speed = int(input("Enter speed (1-5): "))
						d.set_speed(speed)
					elif ctrl == '4' and isinstance(d, Light):
						brightness = int(input("Enter brightness (0-100): "))
						d.set_brightness(brightness)
					elif ctrl == '5' and isinstance(d, ac):
						temperature = int(input("Enter temperature (16-30): "))
						d.set_temperature(temperature)
					elif ctrl == '6' and isinstance(d, WashingMachine):
						mode = input("Enter mode (normal/delicate/heavy): ")
						d.set_mode(mode)
					else:
						print("Invalid option or not supported for this device.")
					break
			if not found:
				print("Device not found.")

		elif choice == '5':
			name = input("Enter device name: ")
			device_found = None
			for d in device_manager.devices:
				if d.name == name:
					device_found = d
					break
			if not device_found:
				print("Device not found. Cannot add schedule.")
			else:
				start_time = input("Enter start time: ")
				end_time = input("Enter end time: ")
				schedule_id = schedule_manager.add_schedule(start_time, end_time, name)
				print(f"Schedule created with ID {schedule_id}.")

		elif choice == '6':
			print("Manage Device Schedule")
			print("a. Update Schedule")
			print("b. Delete Schedule")
			sub_choice = input("Enter your choice: ")
			if sub_choice == 'a':
				schedule_id = int(input("Enter schedule ID to update: "))
				schedule_found = None
				for s in schedule_manager.schedules:
					if getattr(s, 'schedule_id', None) == schedule_id:
						schedule_found = s
						break
				if not schedule_found:
					print("Schedule not found. Cannot update.")
				else:
					start_time = input("Enter new start time (leave blank to keep current): ")
					end_time = input("Enter new end time (leave blank to keep current): ")
					device_name = input("Enter new device name (leave blank to keep current): ")
					updated = schedule_manager.update_schedule(
						schedule_id,
						start_time if start_time else None,
						end_time if end_time else None,
						device_name if device_name else None
					)
					if updated:
						print("Schedule updated.")
					else:
						print("Schedule not found.")
			elif sub_choice == 'b':
				schedule_id = int(input("Enter schedule ID to delete: "))
				schedule_found = None
				for s in schedule_manager.schedules:
					if getattr(s, 'schedule_id', None) == schedule_id:
						schedule_found = s
						break
				if not schedule_found:
					print("Schedule not found. Cannot delete.")
				else:
					deleted = schedule_manager.delete_schedule(schedule_id)
					if deleted:
						print("Schedule deleted.")
					else:
						print("Schedule not found.")
			else:
				print("Invalid choice.")

		elif choice == '7':
			schedules = schedule_manager.view_schedules()
			if not schedules:
				print("No schedules found.")
			else:
				for s in schedules:
					print(f"ID: {s['id']}, Device: {s['device']}, Start: {s['start_time']}, End: {s['end_time']}")

		elif choice == '8':
			print("Exiting Smart Home Program.")
			break
		else:
			print("Invalid choice. Please try again.")

if __name__ == "__main__":
	main()
