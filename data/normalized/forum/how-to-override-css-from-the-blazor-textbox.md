# How to override CSS from the Blazor TextBox?

## Question

**Phi** asked on 17 Jul 2022

Hey! Atm I'm trying to override the styling of the Telerik TextBox. It currently looks like this; Im using a light theme and trying to change the border of the inner input of the TextBox. All i change doesn't seem to work. I tried stuff like this : /*.k-textbox:focus, .k-textbox:active{ border-color: transparent; border: none; } .k-textbox-container, .k-textbox-container:active{ border-color:transparent; border:none; } .k-input:focus, .k-input:active{ border-color: none; border: none; }*/ But I can't find a proper documentation for the inner styling of the TextBox input. All I want to change is the visibility of the input border. Thanks for reading this post. Phil

## Answer

**Hristian Stefanov** answered on 20 Jul 2022

Hi Philipp, You can modify the TextBox with custom styles by applying them to its default class ".k-textbox " or set a custom Class. Here is an example I have prepared for you: <style>.k-textbox { border: none;
} </style> <div class="box-content" style="margin: auto;"> <TelerikTextBox Width="200px" PlaceHolder="Type your message here"> </TelerikTextBox> </div> Please run and test it to see the result. Regards, Hristian Stefanov Progress Telerik

### Response

**Ben** commented on 31 Aug 2022

Hi Hristian, Can I ask a follow-up question. How can this now be done on a global level? I tried adding the custom class to site's CSS file, but it does not take effect. It works 100% when adding the style locally, but on large system this is not feasible. I want also to take it further by only applying this style based on mediaquery. I need to reduce the input components sizes when the screen size fall below certain threshold. Thank you in advanced. Ben

### Response

**Hristian Stefanov** commented on 05 Sep 2022

Hi Ben, Let's cover the follow-up question below. It is achievable, I confirm, to apply the CSS style based on mediaquery on a global level. You are currently on the right path. Here is how possibly you can add it to the " site.css " file: @media ( max-width: 1200px ) {.k-textbox { border: none!important;
}
} With the above CSS style, if you reduce the screen width to under 1200px, the textbox border will disappear. I have also prepared an example in the attached project (see " textbox-global-mediaquery-style.zip "). Use the attached example as a starting point and configure the mediaquery condition as you like. //Note: The CSS style will apply to every Telerik Blazor UI component that uses TelerikTextBox. To avoid that, you can set a Class to the TelerikTextBox instances and apply the CSS rule to that Class.
