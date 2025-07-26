# Multiple Masks?

## Question

**Mar** asked on 18 Feb 2021

I am debating if I want to use the MaskedTextBox instead of the TextBox. If I use the MaskedTextBox, I would need to give it a collection of masks. For example ISBN-13: 000-0-00000-000-0 ISBN-10 0-00000-000-0 ASIN: AAAAAAAAAA Thanks -marc

## Answer

**Marin Bratanov** answered on 19 Feb 2021

Hi Marc, I am afraid that such logic is impossible for a masked textbox component. The masks can have too many differences in the input they must allow and it is impossible for the component to know when and how to switch between them. You could perhaps make the first three zeroes optional for ISBN 10 (see the "9" rule ), or see about masking it with literals, and combine both ISBN settings into one, but the other number is decidedly different. Perhaps you could have another setting (dropdown or radio buttons) that let the user choose the type of number they want to input and that toggles the mask into one of the options, or even switches out entire component instances so you can have varying settings between them. Regards, Marin Bratanov

### Response

**Marc Simkin** answered on 25 Feb 2021

Understood and closed.
