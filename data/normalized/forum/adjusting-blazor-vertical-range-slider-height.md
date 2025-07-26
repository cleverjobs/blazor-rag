# Adjusting Blazor Vertical Range Slider height?

## Question

**Jst** asked on 03 Jun 2021

I understand how to make the range slider fill a horizontal space using Width but is there a way to make a Vertical Range Slider fill a vertical space?

## Answer

**Dimo** answered on 08 Jun 2021

Hello John, Yes, the vertical RangeSlider can be expanded to 100% height with a custom CSS class: <div style="height:600px;background:#ffe"> <TelerikRangeSlider @bind-StartValue="@Value" @bind-EndValue="@EndValue" Orientation="@SliderOrientation.Vertical" SmallStep="10" LargeStep="20" Min="0" Max="100" Class=" expand-slider "> </TelerikRangeSlider> </div> <style>.k-slider-vertical.expand-slider { height: 100%;
} </style> @code {
public int Value { get; set; }=30;
public int EndValue { get; set; }=70;
} The above colored <div> is for illustration purposes only. Note that percentage heights require the parent element to have an explicit height. If the parent has a percentage height too, the rule is applied recursively until the <html> element is reached, or until an element with a fixed height is reached. This is discussed also at: [https://docs.telerik.com/blazor-ui/common-features/dimensions](https://docs.telerik.com/blazor-ui/common-features/dimensions) Regards, Author nickname Progress Telerik
