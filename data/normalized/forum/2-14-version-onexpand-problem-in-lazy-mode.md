# 2.14 version OnExpand problem in Lazy mode

## Question

**And** asked on 26 May 2020

Hello, Marin. After upgrade from 2.12 to 2.14 version I have a problem When I expand a node, I have exception. Microsoft.AspNetCore.Components.Server.Circuits.RemoteRenderer: Warning: Unhandled exception rendering component: Object reference not set to an instance of an object. System.NullReferenceException: Object reference not set to an instance of an object. at Telerik.Blazor.Components.TreeView.TreeViewNode.ToggleAnimationContainerAsync() at Telerik.Blazor.Components.TreeView.TreeViewNode.ToggleExpand() at Microsoft.AspNetCore.Components.ComponentBase.CallStateHasChangedOnAsyncCompletion(Task task) at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle) Microsoft.AspNetCore.Components.Server.Circuits.CircuitHost: Error: Unhandled exception in circuit 'hyHyoH3D6-TdzHqjUEAgnTTMn8agGOfRQaRZTjj0xzs'. Microsoft.AspNetCore.Components.Server.Circuits.RemoteRenderer: Warning: Unhandled exception rendering component: Cannot process pending renders after the renderer has been disposed. Object name: 'Renderer'. Even if I'm not use OnExpand event I have same problem in 2.14. In 2.12 all works fine. Thank you.

## Answer

**Marin Bratanov** answered on 27 May 2020

Thank you for reaching out, Andriy. I made this page where you can Follow the status of the bug: [https://feedback.telerik.com/blazor/1469127-when-using-onexpand-you-get-object-reference-not-set-to-an-instance-of-an-object.](https://feedback.telerik.com/blazor/1469127-when-using-onexpand-you-get-object-reference-not-set-to-an-instance-of-an-object.) By the way, we're working on selection and node click event in the treeview. Regards, Marin Bratanov
