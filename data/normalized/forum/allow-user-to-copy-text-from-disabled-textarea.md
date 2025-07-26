# Allow user to copy text from Disabled TextArea

## Question

**Ale** asked on 07 Nov 2020

now it is not possible, at least in FF

## Answer

**Marin Bratanov** answered on 11 Nov 2020

Hello, You can Follow the implementation of such a feature here: [https://feedback.telerik.com/blazor/1483630-allow-selecting-and-copying-text-from-inputs-with-enabled-false.](https://feedback.telerik.com/blazor/1483630-allow-selecting-and-copying-text-from-inputs-with-enabled-false.) I see that you've already added your Vote to it, and you can also click the Follow button to get email notifications for status updates. I've also added a workaround in the initial post that you can consider: <style> /* re-enable pointer events for the inputs so selection can work. Note - can cause some side effects with appearance of hover and focus states */.k-input.k-state-disabled, input.k-textbox [disabled] { pointer-events: initial;
} /* visual highlight for the plain textbox user selection */ input.k-textbox [disabled]::selection { color: #ffffff; background-color: #ff6358;
} </style> <TelerikTextBox @bind-Value="@tbText" Enabled="false" /> <TelerikTextArea @bind-Value="@taText" Enabled="false" /> @code{
string tbText { get; set; }="lorem ipsum";
string taText { get; set; }="lorem ipsum\ndolor sit amet";
} Regards, Marin Bratanov
