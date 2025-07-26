# MultiSelect in a ListView as a Navigation Property Collection

## Question

**Chr** asked on 17 Dec 2024

I want to have a MultiSelect experience for a field in a ListView editor. I'd like the binding to work with the model's navigation collection instead of an ancillary Id collection. Take the following example where we have a ListView of Appointments. An Appointment has a collection of Contacts called Attendees that we want to manage on Create and Edit with a MultiSelect. TelerikMultiSelect doesn't like a bind-value with a collection of objects - it wants Ids. One way to solve this could be to do gymnastics with an extra AttendeeIds collection on the Appointment and synchronize that collection with the navigation entities on read/create/update. Is there a way to avoid the gymnastics and solve this case more directly? Can you provide an example? Thanks. <TelerikListView TItem="Appointment"...> ... <EditTemplate> <TelerikMultiSelect Data="@Contacts" Placeholder="Select attendees" AutoClose="false" @bind-Value="@context.Attendees" <-this does not work TextField="@nameof(Contact.Name)" ValueField="@nameof(Contact.Id)" DebounceDelay="0" /> </EditTemplate> ... </TelerikListView> List <Contact> Contacts {get; set;}=[]; //loaded in oninitializeasync

public class Appointment {
public Guid Id {get; set;}
public List <Contact> Attendees {get; set;}
}

public class Contact {
public Guid Id {get; set;}
public string Name {get; set;}
} ...

## Answer

**Hristian Stefanov** answered on 18 Dec 2024

Hi Christopher, To achieve the desired functionality of binding the TelerikMultiSelect component directly to a model's navigation collection, a workaround is necessary because the MultiSelect requires binding to a collection of primitive values rather than complex objects. Here's how you can handle this scenario: Approach with Auxiliary Property Auxiliary Property: Use a property to hold the IDs of the selected contacts, which will be bound to the MultiSelect. Synchronization Logic: Implement logic to sync this auxiliary property with the navigation property when loading and saving data, ensuring the UI reflects the model's state and vice versa. Example Implementation The example below is for demonstration purposes. <TelerikListView TItem="Appointment" Data="@Appointments"> <EditTemplate> <TelerikMultiSelect Data="@Contacts" Placeholder="Select attendees" AutoClose="false" @bind-Value="@AttendeeIds" TextField="@nameof(Contact.Name)" ValueField="@nameof(Contact.Id)" DebounceDelay="0" /> </EditTemplate> </TelerikListView> @code {
List <Appointment> Appointments { get; set; }=new List <Appointment> ();
List <Contact> Contacts { get; set; }=new List <Contact> ();

// This property will hold the selected contact IDs for the MultiSelect
List <Guid> AttendeeIds { get; set; }=new List <Guid> ();

protected override async Task OnInitializedAsync()
{
// Load your contacts and appointments here
// Example contacts
Contacts=new List <Contact> {
new Contact { Id=Guid.NewGuid(), Name="Alice" },
new Contact { Id=Guid.NewGuid(), Name="Bob" },
new Contact { Id=Guid.NewGuid(), Name="Charlie" }
};

// Example appointment
Appointments=new List <Appointment> {
new Appointment { Id=Guid.NewGuid(), Attendees=new List <Contact> { Contacts[0], Contacts[1] } }
};

// Initialize AttendeeIds based on the current appointment's attendees
AttendeeIds=Appointments.First().Attendees.Select(a=> a.Id).ToList();
}

// Call this method when saving the appointment
void SaveAppointment()
{
var appointment=Appointments.First();
appointment.Attendees=Contacts.Where(c=> AttendeeIds.Contains(c.Id)).ToList();
}

public class Appointment
{
public Guid Id { get; set; }
public List <Contact> Attendees { get; set; }
}

public class Contact
{
public Guid Id { get; set; }
public string Name { get; set; }
}
} Summary Auxiliary Property (AttendeeIds): This property is bound to the MultiSelect and stores the IDs of the selected contacts. Synchronization: On initialization, populate AttendeeIds from the Attendees navigation property. When saving, update Attendees using the IDs in AttendeeIds. This method provides a clear pathway to manage the attendees using the MultiSelect component without directly binding complex objects, thus avoiding the need for extensive workarounds or "gymnastics." Regards, Hristian Stefanov Progress Telerik
