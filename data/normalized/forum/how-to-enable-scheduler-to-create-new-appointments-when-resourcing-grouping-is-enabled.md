# How to enable Scheduler to create new Appointments when resourcing grouping is enabled

## Question

**Pau** asked on 16 Oct 2023

Hi there We have a Scheduler with three resources defined which is working as expected. I've removed a bunch of tags for simplicity: <TelerikScheduler Data="@Flights" AllowCreate="true" AllowDelete="false" AllowUpdate="true" OnEdit="@Edit"> <SchedulerResources> <SchedulerResource Field="@nameof(Flight.SquadronEntityRowId)" Title="Squadron" Data="@_allSquadrons" TextField="@nameof(Squadron.Name)" ValueField="@nameof(Squadron.SquadronEntityRowId)" /> <SchedulerResource Field="@nameof(Flight.AircraftEntityRowId)" Title="Aircraft" Data="@_allAircraft" TextField="@nameof(Aircraft.TailFinId)" ValueField="@nameof(Aircraft.AircraftEntityRowId)" ColorField="@nameof(Aircraft.Colour)" /> <SchedulerResource Field="@nameof(Flight.AircraftType)" Title="Aircraft Type" Data="@SelectedAircraftTypes" TextField="@nameof(AircraftType.Name)" ValueField="@nameof(AircraftType.AircraftTypeEntityRowId)" ColorField="@nameof(AircraftType.Color)" /> </SchedulerResources> <SchedulerSettings> <SchedulerGroupSettings Resources="@(new List<string> { nameof(Flight.SquadronEntityRowId) })" Orientation="@SchedulerGroupOrientation.Horizontal"> </SchedulerGroupSettings> </SchedulerSettings> </TelerikScheduler> As you can see, we have grouping defined on one of the resources. This seems to work in the UI (aircraft and groups redacted for client confidentiality): However, despite having set AllowCreate="true", when doubling clicking an empty slot the OnEdit event doesn't fire. If I clear resource grouping however, double clicking then fires the edit event as expected: Can someone please help us understand why creating new appointments when resource grouping is on isn't working? Is this intended behaviour? Cheers, Paul

### Response

**Dimo** commented on 17 Oct 2023

Such strange issues usually occur when the component model class doesn't have getters and setters for all properties, or some properties are readonly. If you edit this online demo in REPL and add an OnEdit handler, it will work. Start from here.

### Response

**Paul** commented on 17 Oct 2023

Hi Dimo Thanks again for answering so quickly. Yes, I just discovered that was the issue and hadn't yet circled back here to update the thread. I did in fact NOT have a setter on the property. I guess the issue is that the Scheduler swallowed the exception and when it errored it did so quietly. To my mind if there's an error like that, exceptions should be raised and not caught so that the issue is more transparent. Cheers, Paul

### Response

**Dimo** commented on 17 Oct 2023

As far as I remember, the exception is not caught, but it occurs outside our assembly, that's why it doesn't show in the browser. However, if you run your project with our source code attached (instead of the NuGet package), you will see the exception in the Visual Studio's Output window.
