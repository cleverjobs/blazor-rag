# DockManager flickers when restoring state after navigation

## Question

**Boh** asked on 17 Jun 2025

Hi, I need some help with the DockManager. Is it currently possible to prevent the flickering/loading effect when navigating to a page and restoring the DockManagerState from local storage? Once I pin delegate(with setting state inside directly to args or with SetState method) to OnStateInit (because I want to control Layout state and reapply it when navigating) -> it starts flickering loading. Once I don't pin to OnStateInit(with the same delegate mech I discribed earlier) -> everything works fine, but state can't be saved and recreated. The behavior looks like a short reload or UI flicker when the state is reapplied. I followed the setup exactly as shown in the official Demo, but seems like it is working nice only after DockManager is fully rendered and then changing it's state. Thanks in advance!

## Answer

**Dimo** answered on 18 Jun 2025

Hello Bohdan, By design, the DockManager shows a LoaderContainer automatically when it has an OnStateInit event handler. You can disable this loader container with a bit of custom CSS. .k-dock-manager>.k-loader-container { display: none;
} Note that after making this change, users with slow internet connection may start noticing how the DockManager rearranges its panes, according to the restored state. Regards, Dimo Progress Telerik

### Response

**Bohdan** commented on 01 Jul 2025

Hi Dimo, Thanks a lot for your response! For those, who may have the same issue: after some debugging, I noticed that the DockManager component was re-initializing every time I navigated between pages. That turned out to be the root cause of the issue I was facing. Thanks again for your support and work on the Telerik components! Best regards, Bohdan
