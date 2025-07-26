# SignalR Updating

## Question

**Ric** asked on 27 May 2019

Do you have any examples yet on updating all clients from any of your controls? Grid changes for example to update every connected client?

## Answer

**Marin Bratanov** answered on 28 May 2019

Hi Rick, The grid exposes a number of events that are fired when the CRUD operations execute, and they let you access the new data, and get notified that something changed. You definitely need to use them to update the actual database (e.g., call a web service or an existing data access layer logic), and perhaps you can add there a call that will perform the desired reloading (maybe a JS interop call to a signalR hub that you already have running). I am not sure how one can reload a view in Blazor, apart from changing data which would re-render relevant parts of the view, though, so once you have that C# logic running, you should be able to call it from the grid events. I must note here a related bug - see this page (I've already added your vote to raise its priority, because it is likely to affect you). That said, if you create such an example, I'd encourage you to post it here and we'll gladly award your contribution with Telerik points. Of, if you prefer, open a pull request in the following repo: [https://github.com/telerik/blazor-ui.](https://github.com/telerik/blazor-ui.) Regards, Marin Bratanov

### Response

**Jonathan** commented on 19 Oct 2021

Is there any thought on including this in upcoming Blazor releases? It would be immensely helpful for an application I'm developing. I cannot find any resources for updating all connected clients to a web application using Blazor Grid.

### Response

**Marin Bratanov** commented on 19 Oct 2021

To be a little blunt, Jonathan, I do not think such a feature will ever be built-in into our component. This is something that is part of the business logic of the app and there are far too many ways for clients to connect, and far too many choices for a UI component to make. I recommend you consider a signalr hub and events that you handle that can be triggered by the grid events, or even using some form of singleton service (or other type of service that can raise events in all clients that consume it) to propagate such events.

### Response

**Jonathan** commented on 19 Oct 2021

Thank you Marin for the reply. I was able to achieve the desired functionality utilizing SqlTableDependency. Here is the link I used to follow: [https://github.com/christiandelbianco/blazor-notification-db-record-change](https://github.com/christiandelbianco/blazor-notification-db-record-change)
