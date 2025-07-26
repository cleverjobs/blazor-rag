# TelerikCard Click

## Question

**Igo** asked on 17 May 2024

Hi there, Is there a way to handle the click anywhere on TelerikCard without wrapping it with a div and handling div.onclick? Regards, Igor

## Answer

**Svetoslav Dimitrov** answered on 22 May 2024

Hello Igor, I can confirm that wrapping the TelerikCard in a <div> with an onclick event is the best way to achieve the desired behavior. Regards, Svetoslav Dimitrov Progress Telerik

### Response

**Igor** commented on 22 May 2024

Can we have a way to handle OnClick out of the box in the future releases? (w/o wrapping manually)

### Response

**Svetoslav Dimitrov** commented on 24 May 2024

Hello Igor, What do you expect an OnClick on the <TelerikCard> to do more than what you can already achieve by wrapping the <TelerikCard> in a <div @onclick>?

### Response

**Igor** commented on 27 May 2024

Hello Svetoslav, I don't expect anything more. I just want to avoid wrapping it manually every time I need it. It's much simpler and more readable, convenient to have <TelerikCard OnClick="@..."> rather than <div @onclick="@..."><TelerikCard> ........

### Response

**Svetoslav Dimitrov** commented on 29 May 2024

Hello Igor, You can wrap the TelerikCard, wrapped in a <div @onclick> in a custom component and expose parameters to make an easily reusable component (extract more parameters as needed): <div @onclick="@OnCardClick"> <TelerikCard Width="200px"> <CardHeader> <CardTitle> Card Title </CardTitle> </CardHeader> <CardBody> <CardTitle> Rome </CardTitle> <CardSubTitle> Capital of Italy </CardSubTitle> <CardSeparator> </CardSeparator> <p> Rome is a sprawling, cosmopolitan city with nearly 3,000 years of globally influential art, architecture and culture on display.

Ancient ruins such as the Forum and the Colosseum evoke the power of the former Roman Empire. </p> </CardBody> <CardActions Layout="@CardActionsLayout.Stretch"> <TelerikButton Class="k-flat" Icon="@SvgIcon.HeartOutline" Title="Like"> </TelerikButton> <TelerikButton Class="k-flat" Icon="@SvgIcon.Comment" Title="Comment"> </TelerikButton> <TelerikButton Class="k-flat"> Read More </TelerikButton> </CardActions> <CardFooter> <span style="float:left"> Created by @@john </span> <span style="float:right"> March 05, 2021 </span> </CardFooter> </TelerikCard> </div> <p> Card click event: @Test </p> @code {
private string Test { get; set; }=string.Empty;

private void OnCardClick ( ) {
Test=DateTime.Now.ToLongTimeString();
}
} I can confirm that we have no intention of adding an OnClick event to the whole Card.

### Response

**Lorenzo** commented on 05 Sep 2024

Hi, sorry to jump in but I've tried incapsulating the TelerikCard inside a div with @onclick but nothing seems to happen. Also, I noticed from the code posted above that the onclick event for the div is assigned directly to the EventCallback, shouldn't it instead be assigned to a method that then Invokes that EventCallback? In my speficic case, what I am trying to accomplish is to create a clickable container that also contains other buttons inside, and at the moment is rendered using a TelerikCard. Would this approach work? Or there is another way to do this? Best Regards, Lorenzo

### Response

**Dimo** commented on 05 Sep 2024

@Lorenzo - the existing example was designed to work as a custom .razor component. I simplified it and now it should look the way you expect it to. If it doesn't work on your side, make sure the .razor file is interactive.

### Response

**Lorenzo** commented on 05 Sep 2024

Thanks Dimo for changing the code, however what I'm trying to accomplish here is exactly what you mentioned: having a single component that represent the clickable container (rendered using TelerikCard) that caintains in itself also different action buttons, so the user can choose to click the container only or the action button only. Should this work for InteractiveServer mode in .net8?

### Response

**Dimo** commented on 05 Sep 2024

@Lorenzo - to distinguish clicks on the Card container and on nested clickable elements, you need to wrap the latter in containers with @onclick:stopPropagation. In general, such nested clickability is a bit tricky from UX perspective. And yes, this should work with InteractiveServer mode in .NET 8.

### Response

**Lorenzo** commented on 06 Sep 2024

Thanks Dimo, I've tried but the event does not get triggered. Below a part of my code, inserted inside a Instance.razor component (with OnCardClick function in Instance.razor.cs): <div @onclick="@OnCardClick">
<TelerikCard>
<CardBody>
[...]
</CardBody>
</TelerikCard>
</div>

### Response

**Lorenzo** commented on 06 Sep 2024

I've solved this incorporating a card inside a TelerikButton and it works properly. Thanks anyway for your precious help, Lorenzo P.s. for anyone that might be reading this: the root cause of my issue with div @onclick was that Microsoft.AspNetCore.Components.Web, although being in _Imports.razor, wasn't correctly loaded by the component, so adding a using statement on top of the page made everything work correctly.
