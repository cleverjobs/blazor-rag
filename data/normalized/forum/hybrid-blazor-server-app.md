# Hybrid Blazor Server App

## Question

**Gra** asked on 03 Mar 2020

Hi, I am trying to run a blazor server side component inside a razor view page. So the razor view is this: <div class="wrapper"> @await Html.PartialAsync("_farmMenu", new PfmsWeb.Areas.Shared.ActiveMenu("PickupSequence")) <div id="main" class="sidebar-page main"> <component type="@typeof(PfmsWeb.Components.Harvest.PickupSequence.PickupSequenceShell)" render-mode="ServerPrerendered" /> </div> </div> And the PickupSequenceShell.razor file looks like this: <TelerikRootComponent> Shell Started <br /> <Counter /> </TelerikRootComponent> However, when running the application the counter is not rendered at all. If I reference the counter directly from the razor view it does work. There must something in my understanding that is stopping this from working properly. It cannot be the blazor js as like I said I can run the counter directly from the razor view. This is a very large application so I cannot easily just bring the entire thing into blazor server side, I have to host little blazor server side apps inside the razor views refactoring parts of the application as I go. Has anyone managed to get a hybrid app working on dotnet core with controllers and views?

## Answer

**Grant** answered on 03 Mar 2020

ummm, embarassing... but don't use @for the typeof declaration. And seems components in nested folders are some issue even tho I have all the imports defined. My folders hierarchy was Components/Harvest/PickupSequence/Search moving the search component into the same folder as the shell and it just works. This issue is environmental/user and can be deleted to save further embarrassment from other readers :)

### Response

**Marin Bratanov** answered on 03 Mar 2020

Hello Wayne, Thank you for sharing your experience and solution with the community. I'd rather keep the thread in case someone else has similar issues, unless you explicitly want me to delete it. I would only add that there are a couple of examples in the following repo that can also be helpful and provide some experience we had with razor component (and, mainly, how passing parameters to them from the MVC side of things breaks them): [https://github.com/telerik/blazor-ui/tree/master/common/razor-components](https://github.com/telerik/blazor-ui/tree/master/common/razor-components) Regards, Marin Bratanov
