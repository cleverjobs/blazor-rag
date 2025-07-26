# bUnit test a component that has a TelerikDropZone

## Question

**Jer** asked on 30 Nov 2023

Hi, I am trying to test a component that has a 'TelerikDropZone' inside, I don't need to do any interaction with the drop zone but when I try to render my component (using bUnit) var myCmp=RenderComponent<MyComponent>(); It gives an error System.NullReferenceException: Object reference not set to an instance of an object.

System.NullReferenceException
Object reference not set to an instance of an object.
at Telerik.Blazor.Components.TelerikDropZone..ctor()
at System.RuntimeType.CreateInstanceDefaultCtor(Boolean publicOnly, Boolean wrapExceptions) As best I can tell looking at it, it seems to be coming up from the 'BaseComponent.Localizer' [ Parameter ] public string HintText { get; set; }=BaseComponent.Localizer[ "DropZone_Hint" ]; And if I just comment out the TelerikDropZone my tests run fine. DropZone definition if it helps - <TelerikDropZone Id="myDz"> <Template> <div class="hint"> <i class="far fa-file-plus me-2"> </i> <span> Drag and drop file here </span> </div> </Template> </TelerikDropZone> Is there some extra setup I need to do here in order to get it to work? Thanks!

## Answer

**Dimo** answered on 05 Dec 2023

Hello Jeremy, All our components render UI labels with an ITelerikStringLocalizer, which is initialized in BaseComponent.OnInitializedAsync. Our components use a localization service for consistency even when there is no true localization in the app. Here is how the BaseComponent localizer is assigned. ( InitLocalizer () is called in OnInitializedAsync ) protected void InitLocalizer ( ) { if (Localizer==null )
{ var injectedLocalizer=ServiceProvider?.GetService( typeof (ITelerikStringLocalizer)) as ITelerikStringLocalizer; if (injectedLocalizer !=null ) // depends on builder.Services.AddTelerikBlazor(); in Program.cs {
Localizer=injectedLocalizer;
} else if (RootComponent?.Localizer !=null ) // depends on <TelerikRootComponent Localizer="..." /> {
Localizer=RootComponent?.Localizer;
} else { Localizer=new TelerikStringLocalizer(); }
}
} So, the Localizer should not be null, unless OnInitializedAsync is not executed at all. I am not familiar with the bUnit's internals and how is this even possible. There is a bUnit documentation on a related topic. You can also try setting the HintText parameter explicitly as a workaround, but normally, this shouldn't be necessary and we don't set localization-dependent parameters in our bUnit sample. Regards, Dimo Progress Telerik

### Response

**Jeremy** commented on 08 Dec 2023

Thanks Dimo you are a life-saver! I "borrowed" the 'TelerikTestContext' here and had my tests inherit from it instead of plain 'TestContext' and that fixed the problem. I think it was down to the overrides for 'Render'/'RenderComponent' ensuring the 'TelerikRootComponent' is setup when rendering.

### Response

**Dimo** commented on 08 Dec 2023

Yes, that file also creates a localizer. I am glad it works now.
