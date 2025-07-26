# Mocking TelerikMediaQuery

## Question

**Val** asked on 28 May 2021

Hello, How can I mock TelerikMediaQuery for testing (with bUnit) ? Regards

## Answer

**Marin Bratanov** answered on 28 May 2021

Hi Valeriy, The media query component uses JavaScript, because there is no other way to handle media queries. Thus, it cannot be mocked through the RenderTree. What you can consider is mocking the value it will return. Ultimately, what the component does is to give you an event and a boolean value that you will populate in the view-model. You should mock that value. Regards, Marin Bratanov Progress Telerik
