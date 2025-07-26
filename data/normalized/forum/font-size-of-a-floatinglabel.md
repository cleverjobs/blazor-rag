# Font-Size of a FloatingLabel

## Question

**Hen** asked on 29 Jul 2022

I am new to Telerik (and CSS in generally) and unfortunately I am struggeling even with simple things. I just want to set the Font-Size of a FloatingLabel like this: .floatinglabel {
width: 100%;
color: red;
font-size: 8px;
} The color is red, but the Font-Size is not changing. What am I missing ?

## Answer

**Hristian Stefanov** answered on 03 Aug 2022

Hi Hendrik, I'm ready to help you out. You are on the right path. The CSS selector needs to be slightly different. Here is an example I have prepared for you to demonstrate: <style>.floatinglabel.k-label { color: red; font-size: 8px;
} </style> <TelerikFloatingLabel Class="floatinglabel" Text="Your Name"> <TelerikTextBox Id="name" @bind-Value="@Name" /> </TelerikFloatingLabel> @code {
string Name { get; set; }
} That CSS selector now targets the exact label text. Please run and test it to see the result. Additionally, you can use the browser dev tools to inspect and check the CSS selectors on the current razor page. Regards, Hristian Stefanov Progress Telerik

### Response

**Hendrik** commented on 03 Aug 2022

Hi Hristian, thank you very much. Now I see a lot of things more clearly. The hint with the BrowserDevTools was the key.
