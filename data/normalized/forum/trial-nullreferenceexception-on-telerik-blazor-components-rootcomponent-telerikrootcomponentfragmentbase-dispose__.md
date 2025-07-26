# *Trial* NullReferenceException on Telerik.Blazor.Components.RootComponent.TelerikRootComponentFragmentBase.Dispose()

## Question

**Mic** asked on 29 Jan 2020

Hey everyone, I've been trying Telerik.Blazor on my free time and I happen to have a bit more free time lately. My problem : As soon as I include a custom component with Telerik components in it, i'm having this error when starting the app. Anybody can help my lack of experience? :) Could it be because my trial has expired? QueueViewer_Plans.razor 01. @using Autopost_Config.Data.Controllers; 02. @using Autopost_Config.Data.DAL; 03. 04. @if (plans==null ) 05. { 06. <p><em>Loading...</em></p> 07. } 08. else 09. { 10. <TelerikGrid Data="@plans" Pageable="true" PageSize="10" Sortable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow"> 11. <GridColumns> 12. <GridColumn Field="@(nameof(AutopostPlans.Id))" Title="@(nameof(AutopostPlans.Id))"></GridColumn> 13. <GridColumn Field="@(nameof(AutopostPlans.Task))" Title="@(nameof(AutopostPlans.Task))"></GridColumn> 14. <GridColumn Field="@(nameof(AutopostPlans.DateAjout))" Title="@(nameof(AutopostPlans.DateAjout))"></GridColumn> 15. <GridColumn Field="@(nameof(AutopostPlans.Username))" Title="@(nameof(AutopostPlans.Username))"></GridColumn> 16. <GridColumn Field="@(nameof(AutopostPlans.SendingComputer))" Title="@(nameof(AutopostPlans.SendingComputer))"></GridColumn> 17. <GridColumn Field="@(nameof(AutopostPlans.PathWorkspace))" Title="@(nameof(AutopostPlans.PathWorkspace))"></GridColumn> 18. </GridColumns> 19. </TelerikGrid> 20. } 21. 22. @code { 23. AutopostPlans[] plans; 24. protected override void OnInitialized() 25. { 26. plans=AutopostPlansController.GetAll(); 27. } 28. } Index.razor 01. @page "/" 02. 03. @using Autopost_Config.Data 04. @using Autopost_Config.Components; 05. @using Autopost_Config.Data.Controllers; 06. @using Autopost_Config.Data.DAL; 07. @using Autopost_Config.Data.Services; 08. @inject AutopostDemandesService AutopostDemandesService; 09. 10. <h1>Configuration de l'autopost RBTK</h1> 11. 12. <form> 13. <BlocSelection></BlocSelection> 14. <QueueViewer_Plans></QueueViewer_Plans> 15. @*<QueueViewer_Demandes></QueueViewer_Demandes> 16. <TelerikButton @onclick="@(()=> AutopostDemandesService.createNewDemand())">Lancer l'autopost (Telerik)</TelerikButton>*@17. 18. <div class="form-group row"> 19. <div class="col-sm-10"> 20. <button type="submit" class="btn btn-primary" @onclick="@(()=> AutopostDemandesService.createNewDemand())">Lancer l'autopost</button> 21. </div> 22. </div> 23. </form> 24. 25. @code { 26. 27. }

## Answer

**Michael** answered on 29 Jan 2020

When I go from : <TelerikGrid Data="@plans" Pageable="true" PageSize="10" Sortable="true" FilterMode="Telerik.Blazor.GridFilterMode.FilterRow"> to : <TelerikGrid Data="@plans" Pageable="true" PageSize="10" Sortable="true"> i get a result but non-formatted.

### Response

**Michael** answered on 29 Jan 2020

Nevermind! A updated my Nuget Package and followed this : [https://docs.telerik.com/blazor-ui/getting-started/server-blazor](https://docs.telerik.com/blazor-ui/getting-started/server-blazor) Everything is in order!

### Response

**Michael** answered on 29 Jan 2020

Is there a limitation for Trial that blocks the use of FilterMode in a Grid?

### Response

**Marin Bratanov** answered on 29 Jan 2020

Hello Michael, The issue is probably related to either of these ones: [https://feedback.telerik.com/blazor/1451036-system-objectdisposedexception-cannot-process-pending-renders-after-the-renderer-has-been-disposed-when-i-refresh-a-page-with-f5](https://feedback.telerik.com/blazor/1451036-system-objectdisposedexception-cannot-process-pending-renders-after-the-renderer-has-been-disposed-when-i-refresh-a-page-with-f5) [https://feedback.telerik.com/blazor/1445426-telerik-window-is-causing-following-error-the-current-thread-is-not-associated-with-the-dispatcher](https://feedback.telerik.com/blazor/1445426-telerik-window-is-causing-following-error-the-current-thread-is-not-associated-with-the-dispatcher) I'd suggest giving the upcoming 2.7.0 release a go and testing again. This is the second time we have received such a report yet we have not been able to reproduce the issue and the second fix I linked may help with it. If it doesn't, please open a support ticket and send us a sample where we can observe this problem so we can investigate. In the meantime, I'd suggest trying a Blazor project that is created with our VS extensions: get the extensions: [https://docs.telerik.com/blazor-ui/getting-started/vs-integration/introduction](https://docs.telerik.com/blazor-ui/getting-started/vs-integration/introduction) create a project with them where you can paste the current data: [https://docs.telerik.com/blazor-ui/getting-started/vs-integration/new-project-wizard](https://docs.telerik.com/blazor-ui/getting-started/vs-integration/new-project-wizard) This may give you a working project - the "Grid and menu" template has a filterable grid that works fine on my end. If this runs fine on your end, you can compare the two projects to find the difference causing the problem. Regards, Marin Bratanov

### Response

**Michael** answered on 29 Jan 2020

Thanks Marin for the quick answer! I've tried what you suggested and yes, creating a project from the extension with "Grid and menu" does work perfectly. The problem with my original project seems to be triggered as soon as you have 1 or more columns in a grid. If you call the grid but don't setup any gridcolumns, the page will show. I don't know if that helps in any way but...! I've also compared many files between the original project and the newly created and nothing seems to be off. I'm going to keep digging a little bit. Thanks

### Response

**Marin Bratanov** answered on 30 Jan 2020

Hello Michael, My best guess is that the TelerikRootComponent is either duplicated, or is not at the top of the hierarchy in the problematic project. If copying things over to the new one you got from our extensions is not an option, I'd need you to isolate the grid problem into something small and runnable that I can debug. Without that, it's a guessing game and that's not very efficient. Regards, Marin Bratanov

### Response

**Michael** answered on 30 Jan 2020

Sure, i'll try to come up with something for you in the next few days

### Response

**Michael** answered on 30 Jan 2020

Are you able to access my GitHub repository? I'm pretty new with GitHub, i've been using TFS my entire career mostly. [https://github.com/michaelccote/TelerikGridProblem/tree/master/Autopost_Config](https://github.com/michaelccote/TelerikGridProblem/tree/master/Autopost_Config)

### Response

**Marin Bratanov** answered on 30 Jan 2020

Hi Michael, The problem is that the TelerikRootComponent is missing from the layout: [https://github.com/michaelccote/TelerikGridProblem/blob/master/Autopost_Config/Shared/MainLayout.razor](https://github.com/michaelccote/TelerikGridProblem/blob/master/Autopost_Config/Shared/MainLayout.razor) You can read more about it here: [https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration](https://docs.telerik.com/blazor-ui/getting-started/what-you-need#project-configuration) I also made a pull request with a sample fix for that project: [https://github.com/michaelccote/TelerikGridProblem/pull/1](https://github.com/michaelccote/TelerikGridProblem/pull/1) Regards, Marin Bratanov

### Response

**Michael** answered on 30 Jan 2020

That indeed fixes it! Thank you for your precious time Marin!

### Response

**Marin Bratanov** answered on 30 Jan 2020

You're welcome, Michael, I'm glad I could help. I will now delete my fork to ensure there is no sensitive information from your project exposed from my account, you may want to do the same with your repo (or make it private). Regards, Marin Bratanov
