# System.Threading.Tasks.TaskCanceledException: A task was canceled

## Question

**Rob** asked on 20 Nov 2019

I think I found a bug in all components that use AnimationGroupBase. How you can reproduce it... Navigate to a page that has a component that uses AnimationGroupBase - in my case TreeView. Hit refresh (F5) a couple of times Wait about 60 seconds and you will get an exception from the title.. The problem is AnimationGroupBase. It has a async void Dispose method. Please fix it to be just void. Here is a stack trace. Microsoft.AspNetCore.Components.Server.Circuits.CircuitHost: Error: Unhandled exception in circuit 'uU2u6m_DXs2TW1iUNDEpwJB235BzcJVRHTXjF8kbbaU'. System.Threading.Tasks.TaskCanceledException: A task was canceled. at Microsoft.JSInterop.JSRuntime.InvokeWithDefaultCancellation[T](String identifier, Object[] args) at Telerik.Blazor.Components.AnimationContainer.AnimationGroupBase.Dispose() at System.Threading.Tasks.Task.<>c.<ThrowAsync>b__139_0(Object state) at Microsoft.AspNetCore.Components.Rendering.RendererSynchronizationContext.ExecuteSynchronously(TaskCompletionSource`1 completion, SendOrPostCallback d, Object state) at Microsoft.AspNetCore.Components.Rendering.RendererSynchronizationContext.<>c.<.cctor>b__23_0(Object state) at System.Threading.ExecutionContext.RunInternal(ExecutionContext executionContext, ContextCallback callback, Object state) --- End of stack trace from previous location where exception was thrown --- at System.Threading.ExecutionContext.Run(ExecutionContext executionContext, ContextCallback callback, Object state) at Microsoft.AspNetCore.Components.Rendering.RendererSynchronizationContext.ExecuteBackground(WorkItem item)

## Answer

**Marin Bratanov** answered on 21 Nov 2019

Hello Robert, I can confirm I see this exception in the Debug section of the Ouput window in VS, and reloading the app once is enough so a Dispose is triggered. I do not see the exception in the console, however, and it does not break the app. Is this the behavior you see? Does it break the app on your end? That said, the deeper issue is that Dispose() does not function perfectly well for cleaning up, but there is no better hook in the framework (at the moment). You can read more about this here: [https://github.com/aspnet/AspNetCore/issues/13026.](https://github.com/aspnet/AspNetCore/issues/13026.) Nevertheless, I have forwarded this to the dev team for review and we will see if we can do something to avoid this exception. Regards, Marin Bratanov

### Response

**Robert** commented on 21 Nov 2019

Marin, I'm seeing the same behavior. It does not break the circut but it's not "nice" to have unhandled exceptions in the app. Thank you

### Response

**Marin Bratanov** commented on 21 Nov 2019

Yes, it would be best if there are no such exceptions. In an SPA I'm wary of the potential memory leak if we don't dispose what we need to dispose, though. So if there is nothing we can do right now it is likely that we will keep the exception to avoid a memory leak. Regards, Marin Bratanov
