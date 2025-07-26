# Buttons always have *-rounded-md class

## Question

**Nat** asked on 05 Sep 2022

I generated a new stylesheet using the Telerik Themebuilder and specified that the border-radius should be 0px, but after using the stylesheet in my project, I saw that all my buttons have a border-raduis, which is not the desired effect. Upon further inspection, I saw that this HTML is generated from my TelerikButton. HTML: <button class="telerik-blazor k-button k-button-solid k-rounded-md k-button-rectangle k-button-md k-button-solid-primary k-disabled" id="contracten-laden-button" data-id="eaee6bb5-7628-4584-861d-c02fe6f432a1" tabindex="-1" aria-disabled="true" disabled="" type="submit"> <span class="k-button-text"> Contracten laden </span> </button> TelerikButton: <TelerikButton ThemeColor="@ThemeConstants.Button.ThemeColor.Primary">
Contracten laden
<TelerikLoader ThemeColor="@ThemeConstants.Loader.ThemeColor.Light" Type="@LoaderType.Pulsing" Visible="@IsContracteringsStatussenLoading" />
</TelerikButton> Upon further inspection, I saw within the computed style (in the Developer tools) that the radius is coming from the stylesheet file which I just generated. More specifically, the .k-rounded-md class, which gives a border radius of 4px. It seems like, currently, it is not possible to generate a css file with a border-radius of 0. I suppose that I have to manually change these values, but I fear that I may break some other functionality. Could you please suggest possible solutions? Perhaps specify which classes I could change to 0px to ensure that nothing else breaks. Thank you in advance for your response. I have attached all the files which were generated from the themebuilder, just for completion. Kind regards, Natasha

## Answer

**Joana** answered on 08 Sep 2022

Hello Natasha, Thank you for your report. We are actively working on the ThemeBuilder offering. In mid September we will release a new version that will allow the creation of a theme that supports all customizations of the button styling. In the meantime, the rounded values are controlled by the Rounded parameter of the TelerikButton component. Thus, you can set it to any of the predefined values illustrated in the following appearance demo: [https://demos.telerik.com/blazor-ui/button/appearance](https://demos.telerik.com/blazor-ui/button/appearance) Or you can set it to `none` (not existing value) to remove radius. I have created a REPL snippet where you can test the behavior: [https://blazorrepl.telerik.com/mmkNYClE39qFiMDU12](https://blazorrepl.telerik.com/mmkNYClE39qFiMDU12) Regards, Joana Progress Telerik
