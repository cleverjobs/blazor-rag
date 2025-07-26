# Compiler Error CS0012 after Update to 2.26

## Question

**Mat** asked on 04 Aug 2021

Hi After the update I get the following error message: /...Views/ViewRoute.razor( 13, 13 ): Error CS0012: The type 'SortDescriptor' is defined in an assembly that is not referenced. You must add a reference to assembly 'Telerik.DataSource, Version=2.0.10.0, Culture=neutral, PublicKeyToken=29ac1a93ec063d92'. (CS0012) the package is installed...nevertheless I get the error <PackageReference Include="Telerik.UI.for.Blazor" Version="2.26.0" />
<PackageReference Include="Telerik.DataSource" Version="2.0.10" /> yet I get the error at this position GridState<Wegpunkte> desiredState=new GridState<Wegpunkte>()
{ SortDescriptors=new List<SortDescriptor>() { new SortDescriptor {Member="TourPos", SortDirection=ListSortDirection.Ascending} }
}; is there a solution for this? Thank you very much

## Answer

**Joana** answered on 04 Aug 2021

Hi all, There was a temporary issue with our download management system that was successfully resolved. Please, 1. Delete the Nuget cache - You could use VS to delete the whole Nuget Cache Tools=> Nuget Package Manager=> Package Manager Settings=> General=> Clear All Nuget Cache button - You could delete the Telerik packages cache from C:\Users\[USERNAME]\.nuget\packages telerik.datasource> 2.0.10 folder telerik.ui.for.blazor> 2.26.0 folder 2. Install the Blazor package again - Telerik.DataSource version is updated to 2.0.11 with our 2.26 release. I apologize for the caused inconvenience. I hope that everything will work as expected. Regards, Joana

### Response

**Matthias** commented on 04 Aug 2021

just tested - everything is now working again Thank you

### Response

**Ivan** commented on 04 Aug 2021

You are wonderful! Gantt charts will definitely be a source of inspiration!

### Response

**Ivan** answered on 04 Aug 2021

The same problem. Compilation is not possible after upgrade

### Response

**Jozef** answered on 04 Aug 2021

I have the same problem after update to 2.26.0.

### Response

**Matthias** answered on 04 Aug 2021

I have just created a ticket. Commenting out the affected source code lets the application compile -naturally- without these features. Ticket - Bug
