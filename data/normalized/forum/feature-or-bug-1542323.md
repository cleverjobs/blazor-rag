# Feature or Bug!

## Question

**Mar** asked on 09 Nov 2021

I am trying to style the TexArea component. Unfortunately the class attribute only affects the span wrapper element, Why? I found that this is expected after reading the manual, so it's not a bug or is it (-. I ended up using the standard textarea

## Answer

**Marin Bratanov** answered on 09 Nov 2021

Hi Martin, The Class of the component should render on its main wrapping element in general. This lets you cascade through it to provide styling to all elements inside. Otherwise, there will be elements you can't target, and you won't be able to target the topmost element of the component. Here's an example of such cascades I made for you: <style>.my-class textarea { color: red;
}.my-class.k-label { color: cyan;
} </style> <TelerikTextArea Class="my-class" Label="see the html with the label"> </TelerikTextArea> Regards, Marin Bratanov

### Response

**Martin Herløv** answered on 10 Nov 2021

Of course this is possible but still a surprise that you wrap the textarea in a span. Sometimes the component abstraction layer confuses me (: This old dog need to learn some new tricks.

### Response

**Marin Bratanov** commented on 11 Nov 2021

That's a rather common trend in the component suite - we often have a wrapping element even over things that seem simple, because we add functionality that often does not exist in the plain html counterpart, and that usually requires some cascades, and extra elements, so we need to keep everything contained.
