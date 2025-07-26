# Inline Editing + EF Core Proxy?

## Question

**Por** asked on 15 Nov 2019

I can't get inline editing to work when the item is an EF Core 2.2.6 proxy (lazy loading turned on), it throws an exception right after the OnEdit event. When using POCOs, everything works fine. Not a big issue, but guessing a lot of people might run into this scenario.

## Answer

**Portia** answered on 15 Nov 2019

System.Reflection.TargetInvocationException: Exception has been thrown by the target of an invocation. ---> System.NotImplementedException: This is a DynamicProxy2 error: The interceptor attempted to 'Proceed' for method 'Void set_LazyLoader(Microsoft.EntityFrameworkCore.Infrastructure.ILazyLoader)' which has no target. When calling method without target there is no implementation to 'proceed' to and it is the responsibility of the interceptor to mimic the implementation (set return value, out arguments etc) at Castle.DynamicProxy.AbstractInvocation.ThrowOnNoTarget()

### Response

**Marin Bratanov** answered on 18 Nov 2019

Hi Portia, Are you using the latest versions of the packages? Could you try tomorrow when we ship 2.4.0 that will support .NET Core 3.1 Preview 3? Also, what is the stack trace of this error? How does it include the Telerik components? Do you have a local collection where the data is stored, and can you confirm that the model fields have both a getter and a setter? If you can open a support ticket and send me a runnable MVCE that showcases the Telerik problem, that would be very helpful because this is the first report of this kind that we get. Regards, Marin Bratanov

### Response

**Marco** answered on 31 Jan 2020

Hi there, I've the same issue here: inline editing with lazy loading on the latest blazor server side telerik package Microsoft.AspNetCore.Components.Server.Circuits.RemoteRenderer: Warning: Unhandled exception rendering component: Object reference not set to an instance of an object. System.NullReferenceException: Object reference not set to an instance of an object. at Telerik.Blazor.Components.Grid.GridContentCell`1.get_PropInfo() at Telerik.Blazor.Components.Grid.GridContentCell`1.get_Value() at Telerik.Blazor.Components.Grid.GridContentCell`1.BuildRenderTree(RenderTreeBuilder __builder) at Microsoft.AspNetCore.Components.Rendering.ComponentState.RenderIntoBatch(RenderBatchBuilder batchBuilder, RenderFragment renderFragment) at Microsoft.AspNetCore.Components.RenderTree.Renderer.RenderInExistingBatch(RenderQueueEntry renderQueueEntry) at Microsoft.AspNetCore.Components.RenderTree.Renderer.ProcessRenderQueue() Microsoft.AspNetCore.Components.Server.Circuits.CircuitHost: Error: Unhandled exception in circuit '-ctJ-ctr0bp4mytl5k9AxUWcoK3LyC8ybsC6BxFhGhA'. System.NullReferenceException: Object reference not set to an instance of an object. at Telerik.Blazor.Components.Grid.GridContentCell`1.get_PropInfo() at Telerik.Blazor.Components.Grid.GridContentCell`1.get_Value() at Telerik.Blazor.Components.Grid.GridContentCell`1.BuildRenderTree(RenderTreeBuilder __builder) at Microsoft.AspNetCore.Components.Rendering.ComponentState.RenderIntoBatch(RenderBatchBuilder batchBuilder, RenderFragment renderFragment) at Microsoft.AspNetCore.Components.RenderTree.Renderer.RenderInExistingBatch(RenderQueueEntry renderQueueEntry) at Microsoft.AspNetCore.Components.RenderTree.Renderer.ProcessRenderQueue() [2020-01-31T17:09:22.390Z] Error: System.NullReferenceException: Object reference not set to an instance of an object. at Telerik.Blazor.Components.Grid.GridContentCell`1.get_PropInfo() at Telerik.Blazor.Components.Grid.GridContentCell`1.get_Value() at Telerik.Blazor.Components.Grid.GridContentCell`1.BuildRenderTree(RenderTreeBuilder __builder) at Microsoft.AspNetCore.Components.Rendering.ComponentState.RenderIntoBatch(RenderBatchBuilder batchBuilder, RenderFragment renderFragment) at Microsoft.AspNetCore.Components.RenderTree.Renderer.RenderInExistingBatch(RenderQueueEntry renderQueueEntry) at Microsoft.AspNetCore.Components.RenderTree.Renderer.ProcessRenderQueue() [2020-01-31T17:09:22.393Z] Information: Connection disconnected. Microsoft.AspNetCore.Components.Server.Circuits.RemoteRenderer: Warning: Unhandled exception rendering component: Exception has been thrown by the target of an invocation. System.Reflection.TargetInvocationException: Exception has been thrown by the target of an invocation. ---> System.NotImplementedException: This is a DynamicProxy2 error: The interceptor attempted to 'Proceed' for method 'Void set_LazyLoader(Microsoft.EntityFrameworkCore.Infrastructure.ILazyLoader)' which has no target. When calling method without target there is no implementation to 'proceed' to and it is the responsibility of the interceptor to mimic the implementation (set return value, out arguments etc) at Castle.DynamicProxy.AbstractInvocation.ThrowOnNoTarget() at Castle.DynamicProxy.Internal.CompositionInvocation.EnsureValidTarget() at Castle.Proxies.Invocations.IProxyLazyLoader_set_LazyLoader.InvokeMethodOnTarget() at Castle.DynamicProxy.AbstractInvocation.Proceed() at Castle.DynamicProxy.StandardInterceptor.PerformProceed(IInvocation invocation) at Castle.DynamicProxy.StandardInterceptor.Intercept(IInvocation invocation) at Castle.DynamicProxy.AbstractInvocation.Proceed() at Castle.Proxies.AttivitaProxy.set_LazyLoader(ILazyLoader value) --- End of inner exception stack trace --- at System.RuntimeMethodHandle.InvokeMethod(Object target, Object[] arguments, Signature sig, Boolean constructor, Boolean wrapExceptions) at System.Reflection.RuntimeMethodInfo.Invoke(Object obj, BindingFlags invokeAttr, Binder binder, Object[] parameters, CultureInfo culture) at System.Reflection.RuntimePropertyInfo.SetValue(Object obj, Object value, BindingFlags invokeAttr, Binder binder, Object[] index, CultureInfo culture) at System.Reflection.RuntimePropertyInfo.SetValue(Object obj, Object value, Object[] index) at Telerik.Blazor.Components.TelerikGridBase`1.Clone(TItem original) at Telerik.Blazor.Components.TelerikGridBase`1.Edit(GridCommandEventArgs args) at Telerik.Blazor.Components.TelerikGridBase`1.ExecuteCommand(Object args) at Microsoft.AspNetCore.Components.ComponentBase.CallStateHasChangedOnAsyncCompletion(Task task) at Telerik.Blazor.Components.Grid.GridRowBase`1.OnExecuteCommand(GridCommandEventArgs commandArgs) at Microsoft.AspNetCore.Components.ComponentBase.CallStateHasChangedOnAsyncCompletion(Task task) at Telerik.Blazor.Components.Grid.GridContentCell`1.ExecuteCommandAsync(String commandName) at Telerik.Blazor.Components.Grid.GridContentCell`1.EditAsync() at Telerik.Blazor.Components.Grid.GridContentCell`1.OnClick() at Microsoft.AspNetCore.Components.ComponentBase.CallStateHasChangedOnAsyncCompletion(Task task) at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle) Microsoft.AspNetCore.Components.Server.Circuits.CircuitHost: Error: Unhandled exception in circuit '-ctJ-ctr0bp4mytl5k9AxUWcoK3LyC8ybsC6BxFhGhA'. System.Reflection.TargetInvocationException: Exception has been thrown by the target of an invocation. ---> System.NotImplementedException: This is a DynamicProxy2 error: The interceptor attempted to 'Proceed' for method 'Void set_LazyLoader(Microsoft.EntityFrameworkCore.Infrastructure.ILazyLoader)' which has no target. When calling method without target there is no implementation to 'proceed' to and it is the responsibility of the interceptor to mimic the implementation (set return value, out arguments etc) at Castle.DynamicProxy.AbstractInvocation.ThrowOnNoTarget() at Castle.DynamicProxy.Internal.CompositionInvocation.EnsureValidTarget() at Castle.Proxies.Invocations.IProxyLazyLoader_set_LazyLoader.InvokeMethodOnTarget() at Castle.DynamicProxy.AbstractInvocation.Proceed() at Castle.DynamicProxy.StandardInterceptor.PerformProceed(IInvocation invocation) at Castle.DynamicProxy.StandardInterceptor.Intercept(IInvocation invocation) at Castle.DynamicProxy.AbstractInvocation.Proceed() at Castle.Proxies.AttivitaProxy.set_LazyLoader(ILazyLoader value) --- End of inner exception stack trace --- at System.RuntimeMethodHandle.InvokeMethod(Object target, Object[] arguments, Signature sig, Boolean constructor, Boolean wrapExceptions) at System.Reflection.RuntimeMethodInfo.Invoke(Object obj, BindingFlags invokeAttr, Binder binder, Object[] parameters, CultureInfo culture) at System.Reflection.RuntimePropertyInfo.SetValue(Object obj, Object value, BindingFlags invokeAttr, Binder binder, Object[] index, CultureInfo culture) at System.Reflection.RuntimePropertyInfo.SetValue(Object obj, Object value, Object[] index) at Telerik.Blazor.Components.TelerikGridBase`1.Clone(TItem original) at Telerik.Blazor.Components.TelerikGridBase`1.Edit(GridCommandEventArgs args) at Telerik.Blazor.Components.TelerikGridBase`1.ExecuteCommand(Object args) at Microsoft.AspNetCore.Components.ComponentBase.CallStateHasChangedOnAsyncCompletion(Task task) at Telerik.Blazor.Components.Grid.GridRowBase`1.OnExecuteCommand(GridCommandEventArgs commandArgs) at Microsoft.AspNetCore.Components.ComponentBase.CallStateHasChangedOnAsyncCompletion(Task task) at Telerik.Blazor.Components.Grid.GridContentCell`1.ExecuteCommandAsync(String commandName) at Telerik.Blazor.Components.Grid.GridContentCell`1.EditAsync() at Telerik.Blazor.Components.Grid.GridContentCell`1.OnClick() at Microsoft.AspNetCore.Components.ComponentBase.CallStateHasChangedOnAsyncCompletion(Task task) at Microsoft.AspNetCore.Components.RenderTree.Renderer.GetErrorHandledTask(Task taskToHandle)

### Response

**Marin Bratanov** answered on 31 Jan 2020

Hi Marco, Judging from the stack trace, it looks like when the grid tries to clone the provided data source, those items are null or otherwise their properties are not populated. The grid needs to clone the data source in order to perform its internal operations (like paging, sorting, etc.) without polluting your actual data. Can you confirm that the models bound to the grid are standalone and their creation does not require the involvement of the server/proxy/context? The models the grid binds to need to be something that can be created locally. Regards, Marin Bratanov

### Response

**Marco** answered on 31 Jan 2020

Hi there, I can't get what do you mean exactly with "standalone" and "can be created locally"

### Response

**Marin Bratanov** answered on 01 Feb 2020

Hi Marco, The grid uses reflection to get fields and their values and then does a "new TItem()" call for the items in the data source. The models needs to allow for that. Another report we had used models generated with a third party tool/framework, and those objects could only be created from a factory in that framework, which prevented the grid from instantiating the models it needs to operate. This is the "remote" creation that is not "standalone" that I was referring to. It is possible that something similar is the cause here - for example, creating a new object in the scenario you have may be requiring a trip to the database or some other pre-requisite that the grid could not know about. Regards, Marin Bratanov

### Response

**Marco** answered on 01 Feb 2020

Hi Marin, I've simplified my code to get rid of the issue. The grid code/Service is very simple, I exclude the issue could be there: <TelerikGrid Data=@Attivitas Height="550px" FilterMode="GridFilterMode.FilterMenu" EditMode="@GridEditMode.Incell" Sortable="true" Pageable="true" PageSize="20" Groupable="false"> <GridColumns> <GridColumn Field="Descrizione" Filterable="false" Reorderable="false" /> [...] public List<Attivita> Attivitas { get; set; } protected override void OnInitialized() { Attivitas=DataService_.GetAttivita<Attivita>(); [...] public List<JarodBlazor2.Data.Attivita> GetAttivita<Attivita>() { List<JarodBlazor2.Data.Attivita> list=dc.Attivita.ToList(); return list; } The Model instead is a bit more complex, but I cant' get what's wrong with that, just some virtual functions and a base class: public class Attivita : JarodEntity { public virtual Commessa Commessa { get; set; } public int? CommessaId { get; set; } public DateTime Data { get; set; } public virtual TipoAttivita Tipo { get; set; } public int TipoId { get; set; } public int Ore { get; set; } } public class JarodEntity { public string Descrizione { get; set; } [Key] public int ID { get; set; } public string Owner { get; set; } public virtual List<Type> GetCustomComponents() { List<Type> lt=new List<Type>(); return lt; } public string GetDbSetName() { return this.GetType().Name; } public virtual List<string> GetIncludeList() { return null; } public virtual TP GetProperty<TP>(String PropertyName) { return (TP)this.GetType().GetProperty(PropertyName).GetValue(this); } public override string ToString() { if (string.IsNullOrWhiteSpace(Descrizione)) return GetDbSetName(); return Descrizione; } public virtual bool Update(JarodEntity je) { var props=je.GetType().GetProperties(); bool mod=false; foreach (var prop in props) { var oldValue=prop.GetValue(je); var newValue=prop.GetValue(this); if (oldValue !=newValue) { prop.SetValue(je, newValue); mod=true; } } return mod; } }

### Response

**Marin Bratanov** answered on 03 Feb 2020

Hi Marco, I am attaching a sample app that runs on the provided code. Can you modify it to showcase the Telerik Grid problem? Regards, Marin Bratanov

### Response

**Marco** answered on 03 Feb 2020

Hi Marin, the issue is about lazy loading in EF, with POCO I've not any issue. So I added a dbcontext and enabled lazy loading, the issue comes up as soon as you enable lazy loading in startup.cs at line 34 [https://energosrlit-my.sharepoint.com/:u:/g/personal/marco_morosini_en-ergo_it/EarOmdEDo7tJuxMNrE3NnKQBcJWT-bKla-3xAA1_bwvnaw?e=Syuc6n](https://energosrlit-my.sharepoint.com/:u:/g/personal/marco_morosini_en-ergo_it/EarOmdEDo7tJuxMNrE3NnKQBcJWT-bKla-3xAA1_bwvnaw?e=Syuc6n)

### Response

**Marco** answered on 04 Feb 2020

Hi Marin, did you get the code?

### Response

**Marin Bratanov** answered on 04 Feb 2020

Hi Marco, Yes, I did, the situation is under review by the dev team at the moment. I wanted to post with findings only, and I will do that once we have anything to say. Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 05 Feb 2020

Hello Marco, Portia, We were able to reproduce the issue and it is under investigation. You can follow its status in the following page I created on your behalf: [https://feedback.telerik.com/blazor/1452386-add-support-for-lazyloadingproxies-in-ef.](https://feedback.telerik.com/blazor/1452386-add-support-for-lazyloadingproxies-in-ef.) At this point we suspect it is related to the interfaces EF generates. Regards, Marin Bratanov
