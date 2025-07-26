# Synchronization buttons and circle

## Question

**Ste** asked on 28 Jan 2021

Hi everybody, the synchronization of buttons and the circle is not working correctly. Sometimes when I use one of the buttons the circle jumps back to zero or it is not moving. It seems that the buttons are using different values as the circle. You can also see this effect when using the online sample for label template ([https://demos.telerik.com/blazor-ui/slider/label-template).](https://demos.telerik.com/blazor-ui/slider/label-template).) Curious: the online sample for overview ([https://demos.telerik.com/blazor-ui/slider/overview)](https://demos.telerik.com/blazor-ui/slider/overview)) seems working correctly. BTW: the same effect exists for RangeSlider component. Best Regards, Stefan

## Answer

**Marin Bratanov** answered on 28 Jan 2021

Hello Stefan, Could you try this locally? It is possible that there is a big latency between you and our demos and that could cause various problems with the server-side flavor that the demos app uses. I am also attaching here a short video from some of my tests so you can confirm if I am missing something, because I can't reproduce such issues. Is there some other action I need to take? How does this reproduce with the range slider considering it does not have buttons? Regards, Marin Bratanov

### Response

**Stefan** answered on 28 Jan 2021

Hi Marin, thx for your answer. I also made a video with my experiences, but I'm not able to attach the ZIP file here. Regards, Stefan

### Response

**Marin Bratanov** answered on 28 Jan 2021

Hello Stefan, You could either open a support ticket where you can add zip files, or you can upload it to some file share like onedrive, dropbox, googledrive. Regards, Marin Bratanov

### Response

**Stefan** answered on 28 Jan 2021

Hi Marin, here is a link with the video that I made: [https://1drv.ms/u/s!AmHsBuOlkqJPiNNfdXb7m6xObD2GxA?e=lwX80F](https://1drv.ms/u/s!AmHsBuOlkqJPiNNfdXb7m6xObD2GxA?e=lwX80F) Regards, Stefan

### Response

**Marin Bratanov** answered on 28 Jan 2021

Hi Stefan, This looks like it could be a latency issue. Could you try running the demo code in a local solution to see if you can reproduce it: <label class="title"> Define price range for the product</label>
<div class="mt-md">
<TelerikSlider @bind-Value="@Value" Min="5.0m" Max="10.0m" SmallStep="0.25m" LargeStep="0.5m" Decimals="2" Width="500px">
<LabelTemplate>
<span class="label-template">@context.ToString( "c1" )</span>
</LabelTemplate>
</TelerikSlider>
</div>

@code { public decimal Value { get; set; }=9.5 m;
}

<style>
.title {
text-align: center;
font-size: 18 px;
color: #656565; }
.label-template {
font-style: italic;
}
</style> Regards, Marin Bratanov

### Response

**Stefan** answered on 28 Jan 2021

Hi Marin, the sliders are embedded inside of a Blazor Webassembly App. The data is binded to a model and after loading the model data the visualized data is not correct. The limits are fixed and the displayed values are correct. But the changeable values are wrong when starting the page. Attached is a screenshot with following controls: - RangeSlider with start values 2 and 5 - Slider with start value 3 - Slider with start value 2 The bar length is right for sliders, for range slider the start position of the bar is not correct. And the position of the circle is always at the beginning after initializing the page data. Regards, Stefan

### Response

**Marin Bratanov** answered on 28 Jan 2021

Hello Stefan, I am still not able to reproduce such problems. Someone else is having similar issues, though, so perhaps something there can also help you see what I am missing from the setup: [https://feedback.telerik.com/blazor/1504323-telerikslider-only-works-properly-if-range-is-a-multiple-of-10](https://feedback.telerik.com/blazor/1504323-telerikslider-only-works-properly-if-range-is-a-multiple-of-10) Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 29 Jan 2021

Hello Stefan, In that thread René caught it - it was a culture issue where a comma was rendered instead of a dot as a decimal separator. A fix is pending testing. Regards, Marin Bratanov

### Response

**Stefan** answered on 01 Feb 2021

Hi Marin, In my environment the slider is working now, but the range slider behaviour is as wrong as before. I made a very simple project where I try to show you the effect: [https://1drv.ms/u/s!AmHsBuOlkqJPiNNfdXb7m6xObD2GxA?e=juSnZy](https://1drv.ms/u/s!AmHsBuOlkqJPiNNfdXb7m6xObD2GxA?e=juSnZy) The page FetchData.razor contains a range slider control with a corresponding model instance. May be it is better to move this thread to range slider section? Regards, Stefan

### Response

**Stefan** answered on 01 Feb 2021

Hi Marin, sorry to say: the slider control is also not working as suspected. I Implemented also a slider control to the sample app, hope it helps. Regards, Stefan

### Response

**Stefan** answered on 01 Feb 2021

Hi Marin, it seems that setting the value of Min property (Slider and Range Slider control) to 0 helps. Regards, Stefan

### Response

**Stefan** answered on 01 Feb 2021

Hi Marin, correction: when setting Min value to 0 and Max value to 10 everything seems working fine. With Min/Max combinations like 0/9 or 1/10 the behaviour of both controls is wrong. Regards, Stefan

### Response

**Marin Bratanov** answered on 01 Feb 2021

Hello Stefan, I see an issue in both the sample sliders if I add something like this in Program.cs which makes the culture be something that uses commas for the decimal separator (I expect that's the default on your machine). I just tried that project (including the culture setting) with the current fix and it seemed to work fine for me, so I expect 2.22.0 will bring this fix for you. You can Follow its status here: [https://feedback.telerik.com/blazor/1504323-slider-handle-has-wrong-position-in-cultures-with-comma-for-a-decimal-separator](https://feedback.telerik.com/blazor/1504323-slider-handle-has-wrong-position-in-cultures-with-comma-for-a-decimal-separator) public static async Task Main ( string [] args ) { var builder=WebAssemblyHostBuilder.CreateDefault(args);
builder.Services.AddTelerikBlazor();
builder.RootComponents.Add<App>( "#app" );

builder.Services.AddScoped(sp=> new HttpClient { BaseAddress=new Uri(builder.HostEnvironment.BaseAddress) }); CultureInfo desiredCulture=new CultureInfo( " de-DE " );
CultureInfo.DefaultThreadCurrentCulture=desiredCulture;
CultureInfo.DefaultThreadCurrentUICulture=desiredCulture; await builder.Build().RunAsync();
} Regards, Marin Bratanov

### Response

**Stefan** answered on 01 Feb 2021

Hi Marin, I checked this by using another culture info ("en-US") and you are right: in this case the visualization was correct. Thank you for support, great work! Regards, Stefan

### Response

**Marin Bratanov** answered on 01 Feb 2021

Thank you for confirming my findings, Stefan, there is always a chance I've missed something (it took me a while to figure out it was the culture, and it was actually Rene who noticed). Regards, Marin Bratanov
