# Grid Filtering crashes when no record

## Question

**Mic** asked on 10 Sep 2020

Hey everyone, I'm not sure it a ticket is already open about this or if it was already adressed but i'm having Null referenced exception on the OnInitializedAsync when i have FilterMode.FilterRow and there are no records yet. Works fine when i change for FilterMode.None.

## Answer

**Michael** answered on 10 Sep 2020

Maybe I can add that I made sure to have @using Telerik.Blazor.Components in _Imports.razor and have the TelerikRootComponent in my MainLayout.razor.

### Response

**Svetoslav Dimitrov** answered on 11 Sep 2020

Hello Michael, As an attached file, you could see a demo application, where I have set up a Grid with FilterRow, which gets data from a service and I have added some Delay to simulate actual network delay. If this application works as expected for you, could you compare it against your own and see if there is any difference that may cause the issue. If this does not help, could you modify the project so that the error you are experiencing is reproducible and we can further investigate? Regards, Svetoslav Dimitrov
