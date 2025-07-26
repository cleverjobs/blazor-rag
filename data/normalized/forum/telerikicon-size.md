# TelerikIcon size

## Question

**Dou** asked on 13 Jul 2020

Is there a way to make a TelerikIcon bigger?

## Answer

**Marin Bratanov** answered on 14 Jul 2020

Hi Doug, You can use CSS to increase their font size and if you want some granularity (as that can affect a lot of components and places), you can cascade through a parent class. Here's an example: <style>.my-specific-icon-container.k-icon,.my-specific-icon-container.k-icon::before { font-size: 48px; width: 48px; height: 48px;
}.k-icon,.k-icon::before { font-size: 64px; width: 64px; height: 64px;
}
</style>
<div class=" my-specific-icon-container ">
<TelerikIcon Icon=" @IconName.Audio" />
</div>
<TelerikIcon Icon="@IconName.Audio" /> Regards, Marin Bratanov

### Response

**George** answered on 25 Nov 2020

It would be awesome if you fixed the TelerikIcon IconClass property.

### Response

**Marin Bratanov** answered on 26 Nov 2020

Hello George, What is the exact problem you are having with this parameter? I'm attaching here a screenshot from the way the sample from the docs works in the default project template. <TelerikIcon IconClass="oi oi-home" /> @* home icon from OpenIconic, assuming you have loaded the font on the page, you can use your own CSS classes and font icon fonts *@Regards, Marin Bratanov
