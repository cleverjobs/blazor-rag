# OnClick event in LinearGuagePointer

## Question

**Ste** asked on 17 Oct 2022

My requirement is for the multiple pointers I am setting on one TelerikLinearGauge to have an OnClick event to open a TelerikWindow Modal when the LinearGaugePointer is mouse clicked. I am unable to use a TelerikButton and need to onClick event to be on the pointer. <TelerikLinearGauge> <LinearGaugeScales> <LinearGaugeScale Min="-360" Max="-0" Vertical="false"> </LinearGaugeScale> </LinearGaugeScales> <LinearGaugePointers> <LinearGaugePointer Value="-200"> <LinearGaugePointerTrack Color="#a9a9a9" Visible="true"></LinearGaugePointerTrack> </LinearGaugePointer> <LinearGaugePointer Value=-340 Color=Blue Shape="@LinearGaugePointerShape.Arrow" Size="25" Margin="25"> </LinearGaugePointer> <TelerikWindow Modal="true" @bind-Visible="@isAreaSurveillanceModalVisible" CloseOnOverlayClick="true"> <WindowTitle> Window Title </WindowTitle> <WindowContent> I am modal, so the page content behind me is not accessible to the user. </WindowContent> <WindowActions> <WindowAction Name="Close"/> </WindowActions> </TelerikWindow> <LinearGaugePointer Value=-210 Color=Grey Shape="@LinearGaugePointerShape.Arrow" Margin="25" Size="25"> </LinearGaugePointer> <LinearGaugePointer Value=-60 Color=Blue Shape="@LinearGaugePointerShape.Arrow" Margin="25" Size="25"> </LinearGaugePointer> </LinearGaugePointers> </TelerikLinearGauge> @code{ bool isAreaSurveillanceModalVisible { get; set; }=false; }

### Response

**Dimo** commented on 20 Oct 2022

Hi Stephen, Our Gauges are designed to display information, without user interaction. I am afraid you will need to think of an alternative approach. I would recommend interface outside the Gauge, but if it's critical to actually click on the pointer, then consider invisible overlay with clickable elements. Naturally, such implementation will depend heavily on position calculations. The example below uses hard-coded values. <div class="gauge-wrapper" style="width:100px"> <TelerikLinearGauge Width="100px" Height="200px"> <LinearGaugePointers> <LinearGaugePointer Value="@PointerValue" Color="green" Shape="LinearGaugePointerShape.Arrow" /> </LinearGaugePointers> </TelerikLinearGauge> <div class="gauge-overlay"> <div class="pointer-clicker" style="top:57px;" @onclick="@OnPointerClick"> </div> </div> </div> <style>.gauge-wrapper { position: relative;
}.gauge-overlay { position: absolute; z-index: 1; top: 0; left: 0; bottom: 0; right: 0; border: 1px solid red;
}.pointer-clicker { position: absolute; left: 60px; width: 10px; height: 10px; border: 1px solid red;
} </style> @code {
int PointerValue { get; set; }=35; async Task OnPointerClick ( ) {

}
}

### Response

**Stephen** commented on 20 Oct 2022

Thanks Dimo, I was afraid of that answer. Just had my fingers crossed. Thanks for the very helpful snippet.
