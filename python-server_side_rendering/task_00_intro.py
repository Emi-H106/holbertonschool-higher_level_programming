import os

def generate_invitations(template, attendees):
    if not isinstance(template, str):
        print(f"Error: Template must be a string.")
        return
    
    if not isinstance(attendees, list) or not all(isinstance(a, dict) for a in attendees):
        print(f"Error: Attendees must be a list of dictionaries.")
        return
    
    if template.strip() == "":
        print("Template is empty, no output files generated.")
        return
    
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return
    
     for idx, attendee in enumerate(attendees, start=1):
        name = attendee.get("name") or "N/A"
        event_title = attendee.get("event_title") or "N/A"
        event_date = attendee.get("event_date") or "N/A"
        event_location = attendee.get("event_location") or "N/A"

        invitation = template
        invitation = invitation.replace("{name}", name)
        invitation = invitation.replace("{event_title}", event_title)
        invitation = invitation.replace("{event_date}", event_date)
        invitation = invitation.replace("{event_location}", event_location)

        output_filename = f"output_{idx}.txt"

        try:
            with open(output_filename, "w") as f:
                f.write(invitation)
            print(f"Generated: {output_filename}")
        except Exception as e:
            print(f"Error writing file {output_filename}: {e}")