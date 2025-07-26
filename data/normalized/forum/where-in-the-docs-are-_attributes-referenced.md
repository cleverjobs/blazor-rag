# Where in the docs are @attributes referenced?

## Question

**Bit** asked on 18 Jun 2020

When Im using a component such as a TelerikButton, there is a property @attributes. Where can I see an example of how / what its used for? Can I place a style string in it ?

## Answer

**BitShift** answered on 18 Jun 2020

Nevermind, thats an example of "attribute splatting". However, the question still stands, is there a way to specify some style value, such as padding on a button within the component markup itself? <TelerikButton OnClick="@OnSaveHandler">Save</TelerikButton><br/> or one way I guess would be to wrap the button in a span and put the style there...

### Response

**Svetoslav Dimitrov** answered on 19 Jun 2020

Hello Randal, The @attributes directive comes from the framework as you have mentioned in your second post. You can read more on why this directive will not be implemented in Telerik UI for Blazor in this page: [https://feedback.telerik.com/blazor/1416978-support-arbitrary-attributes](https://feedback.telerik.com/blazor/1416978-support-arbitrary-attributes) Regarding the styling of the Button. You could use the Class parameter of the component to add a CSS class and cascade some styles through it. Below, you can see a quick code snippet to illustrate that: <style>.mySaveButton.k-button { padding-left: 50px;
}
</style> <TelerikButton OnClick=" @OnSaveHandler " Icon="@IconName.Save" Class="mySaveButton">Save</TelerikButton>

@code { void OnSaveHandler ()
{
//your custom code here
}
} Regards, Svetoslav Dimitrov
