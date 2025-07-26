# BrowserSize functionality

## Question

**Phi** asked on 30 Mar 2021

Hello Am trying to use this new component to get the browser size via below; BlazorSizeKiller.razor @foreach (var kv in MediaSizes) { <TelerikMediaQuery Media="@(kv.Value)" OnChange="(()=> UpdateCurrentSize(kv.Key))"></TelerikMediaQuery> } BlazorSizeKiller.razor.cs public partial class BlazorSizeKiller { [Parameter] public int MaxScreenSize { get; set; }=4000; [Parameter] public int MediaQuerySensitivity { get; set; }=10; [Parameter] public int CurrentSize { get; set; } [Parameter] public EventCallback<int> CurrentSizeChanged { get; set; } readonly IDictionary<int, string> MediaSizes=new Dictionary<int, string>(); protected override void OnParametersSet()=> CreateList(); private async Task UpdateCurrentSize(int media)=> await CurrentSizeChanged.InvokeAsync(media); private void CreateList() { if (MediaSizes.Count==0) { for (int i=10; i <MaxScreenSize; i +=MediaQuerySensitivity) { MediaSizes.Add(i, "(max-width: " + i + "px)"); } } } } Is there a better way to do than this? Or are there any problems with this method? Cheers Phil

## Answer

**Marin Bratanov** answered on 31 Mar 2021

Hi Philip, I'd say that I would recommend actually hooking to the window.resize event rather than creating tons of media query component instances. You can find a very basic example of such a service in this sample project, and in this ready-made package. If you need it on an action like a button click, it is best to use one line of JS Interop to ask for it, than try to guess which media query matches. Regards, Marin Bratanov
