# Text input automatically format currency input

## Question

**Gar** asked on 02 Feb 2023

[https://images.ctfassets.net/yqt11gq08a4r/73J73GVPs7ltrOctP24P2O/26839b1efdd3b5580afa7370bf515db0/currency_input_demo.gif](https://images.ctfassets.net/yqt11gq08a4r/73J73GVPs7ltrOctP24P2O/26839b1efdd3b5580afa7370bf515db0/currency_input_demo.gif) There is currently no component that has automatic currency formatting for Blazor. This is critical feature for business users who work with large amounts. People have no idea what they are typing without focusing out of input box.

## Answer

**Dimo** answered on 06 Feb 2023

Hello Garrett, There are three ways to hint users what to type when they use a NumericTextBox: The non-focused value can show a currency symbol via Format. A non-focused empty nullable NumericTextBox can show a Placeholder. A non-empty automatically focused NumericTextBox can have an associated <label>. Here is a REPL test page to demonstrate the above options. Do I understand correctly that your scenario cannot fit in any of the above three suggestions? What is the exact use case? Regards, Dimo

### Response

**Garrett** commented on 07 Feb 2023

Hi, No, that REPL test page does not demonstrate what I am talking about. If you view the GIF I shared, it's a react masking library that shows the commas of a currency value before you focus out of the input field. This allows you to see the number that you are typing, as you are typing it. Typing 156 billion with cents is not easy when there are so many 0's and you have no idea where you are at

### Response

**Dimo** commented on 09 Feb 2023

Hi Garrett, It seems that I have misunderstood you, sorry about that. I thought that "currency formatting" and "people have no idea what they are typing" refers to the currency symbol. Well, yes - I admit that currently we don't provide a numeric input with a mask, or one that shows a formatted value during typing. Based on our research, this feature cannot be integrated easily in the current NumericTextBox. Surely, if more customers demand it, we will consider a major overhaul of the component UX, similarly to the new keyboard UX that we implemented for the DateInput for version 4.0.
