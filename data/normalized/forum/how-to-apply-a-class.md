# How to apply a Class

## Question

**Jon** asked on 06 May 2020

Hi I'm trying to apply the following Class , like this , but doesn't work.. gets override by the Telerik 'k' classes. How can I apply custom Width / Height? thx .TextBoxLarge { width: 400px; height: 50px; } <TelerikTextBox Class="TextBoxLarge" @bind-Value="@Notes"></TelerikTextBox>

## Answer

**Svetoslav Dimitrov** answered on 06 May 2020

Hello Jonathan, The Telerik TextBox offers a parameter Width where you can set the width of the component. If that does not work for you, below, you can see a code snippet I have made based on your example and as attached file a screenshot of the result. I have also increased the font size to match the TextBox. <style>.TextBoxLarge { width: 400px; height: 50px; font-size: 18px;
} </style> <TelerikTextBox Class="TextBoxLarge" @bind-Value="@userInput"> </TelerikTextBox> @code{
public string userInput { get; set; }
} Regards, Svetoslav Dimitrov

### Response

**Mario** commented on 23 Nov 2022

Hi Dimitrov can we change dynamically the class of a text box. For example i had a radiogroup (blue and Coral ) and i want to change the background color of the text box using: <style> .TextBoxBackcolorblue { background-color: lightblue; } .TextBoxBackcolorcoral { background-color: coral; } </style> Can we? best Regards Mario

### Response

**Jonathan** answered on 06 May 2020

thx.. that works, But if i put it in site.css it does not The <style> needs to be on the page?

### Response

**Jonathan** answered on 06 May 2020

Hi.. Also how do you do 'Multi line'? thx again

### Response

**Svetoslav Dimitrov** answered on 07 May 2020

Hello Jonathan, On the second question, there is an open Feature Request in our Feedback Portal regarding Multiline TextBox. You can see it from this link: [https://feedback.telerik.com/blazor/1443556-multiline-textbox.](https://feedback.telerik.com/blazor/1443556-multiline-textbox.) I added your Vote for it, to raise its priorioty, and you can Follow it to receive email notifications on status updates. On the first question, in order it to work in the site.css file you have to add the k-textbox CSS class in front of the TextBoxLarge in the selector. This is related to the Specificity of CSS. In general, this means how the browser decides which CSS rule to apply. The.k-textbox.TextBoxLarge is more specific than.TextBoxLarge which means that it will have more weight when the browser applies the styles. This can be seen visible if you Inspect the component (right click inside the Textbox and Inspect). In case the selector is .TextBoxLarge it will be lower in the Styles tab of the browser DevTools and its CSS rules will be crossed out. However, if you apply .k-textbox.TextBoxLarge it will move higher in the Styles tab and its rules will be applied. More information on Specificity can be read here: [https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity.](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity.) Below is a sample CSS example of this. site.css file: .k-textbox.TextBoxLarge { width: 400px; height: 50px; font-size: 18px;
} Regards, Svetoslav Dimitrov

### Response

**Shannon** answered on 26 Jan 2021

This information: .k-textbox.TextBoxLarge {
width: 400px;
height: 50px;
font-size: 18px;
} should be in the documentation.

### Response

**Nadezhda Tacheva** answered on 28 Jan 2021

Hi Shannon, This information describes a custom scenario for styling a TextBox component. Therefore it wouldn't be a good fit to include in the documentation. We are trying to keep the documentation as simple and clear as possible using general example data that could be relevant in a lot of scenarios. In the below example the .TextBoxLarge is a custom CSS class to style the TextBox with the desired width and height. When adding custom classes to style the Telerik components, they can in some cases be overridden by the built-in rules we have. This is why it is very important to define the CSS selectors as specific as possible. Speaking of that, you may find this article for improving debugging skills useful in order to easily find the relevant element of a component you need to style in your case. On another note - the original reason for this sample styling was the requirement for a text area component which is now available: [https://demos.telerik.com/blazor-ui/textarea/overview.](https://demos.telerik.com/blazor-ui/textarea/overview.) Regards, Nadezhda Tacheva
