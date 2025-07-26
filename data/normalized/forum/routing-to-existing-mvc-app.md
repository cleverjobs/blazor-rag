# Routing to existing MVC App

## Question

**Ste** asked on 04 Oct 2024

We currently have a legacy MVC application that we want to migrate to Blazor WebAssembly. One of our problems is that, when using navigation to route to a MVC page via NavigationManager (which is done everywhere by Telerik UI), Blazor WebAssembly routes internally to NotFound. We would like to override that behaviour but are facing some issues: 1. We tried overriding the Telerik UI behaviour by overriding the onselect handler on some components (i.e. Drawer). While that works fine not every component that does routing seems to have a corresponding overridable event. 2. We tried overriding the navigation event globally using NavigationManager.RegisterLocationChangingHandler to cancel the navigation event and emit a new one (with forceLoad set to true). This seems to not work. Here is the code of our handler. It is getting called and the event is also cancelled just fine. It just seems that the forceLoad does not get respected in that case: private ValueTask OnLocationChanging ( LocationChangingContext context ) { if (BlazorPages.Internal.Contains(context.TargetLocation))
{ return ValueTask.CompletedTask;
} if (Uri.TryCreate(context.TargetLocation, UriKind.Absolute, out Uri? _))
{ return ValueTask.CompletedTask;
}

context.PreventNavigation();

NavigationManager.NavigateTo(context.TargetLocation, forceLoad: true ); return ValueTask.CompletedTask;
} 3. We tried using anchor tags for routing. While that works fine it is really much work to implement this into every component that is getting used. While components can be made reusable we'd have to re-template some others every time since you can't just copy-paste them from the source project. There is not just that problem but also that anchor tags break the styling at every component that I tried until now and we have to style them correctly which also consumes much time. So, the question here is: What is the correct way to handle this use case? Do we really have to rewrite most components that include anchor tags? Is there maybe an alternating Telerik UI version that actually uses anchor tags instead of programmatical routing (which would be really nice since we would get things like right click to open new tab features)?

## Answer

**Dimo** answered on 08 Oct 2024

Hi Stephan, Have you debugged and verified that the LocationChanging handler logic works as expected? As far as I can see, NavigateTo() fires the LocationChanging event again, so the handler must take that into account. I tested intercepting and overriding location changes with our Drawer and Menu components. It works as expected. See MainLayout.razor in the attached app. On a side note, I confirm that the built-in navigation feature of our components always works with the NavigationManager and doesn't use anchor tags. Regards, Dimo Progress Telerik
