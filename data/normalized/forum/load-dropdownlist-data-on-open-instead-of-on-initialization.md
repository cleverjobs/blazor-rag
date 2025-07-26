# Load DropDownList Data on open instead of on initialization

## Question

**And** asked on 31 May 2022

Hello, Is there any way to load data for a the DropDownList when the Dropdown gets opened, instead of when it gets initialized. I've looked over examples and docs and also tried a workaround with virtualization, but even that loads the first page on intialization. I have a UI with multiple DropDownList instances on the page that might not be interacted with, and I'd like to defer loading the data until the user actually interacts with them. Thank you!

## Answer

**Nadezhda Tacheva** answered on 03 Jun 2022

Hi Andrei, In version 3.6.0 of Telerik UI for Blazor we will expose an OnOpen event for the DropDownList and other dropdown components. You may then handle that event to populate the data in the DropDownList. I have added your vote to keep proper track of the requests for this feature. You may as well follow the item to receive email notifications when its status changes. Regards, Nadezhda Tacheva Progress Telerik
