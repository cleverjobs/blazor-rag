# Adjust space between label and field ?

## Question

**TimTim** asked on 10 Jan 2020

How do I adjust the space between label and field when inputting text?By default it's awfully close to the box.

## Answer

**Marin Bratanov** answered on 10 Jan 2020

Hi Tim, You can render you own <label> element so you can style things as you require, for example: <style>
.my-special-label {
width: 300 px;
border: 1 px solid red;
}

.my-special-label .my-label-text-container {
margin-bottom: 2 em;
display: inline-block;
}
</style>
<label class="my-special-label">
<span class="my-label-text-container">Enter Name:</span>
<TelerikTextBox Width="100%" />
</label> Regards, Marin Bratanov

### Response

**Tim** answered on 11 Jan 2020

Thanks Marin, I think I might have explained it poorly. With "Label" I mean the placeholder value. The one that animates above the field when you start typing. See the attached pics.

### Response

**Marin Bratanov** answered on 11 Jan 2020

Hello Tim, Thank you for the clarification. You can inspect the rendered HTML and its CSS rules in order to devise a heavier rule that will produce the desired results. Following this blog post can help you do that: [https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools.](https://www.telerik.com/blogs/improve-your-debugging-skills-with-chrome-devtools.) Here's an example I made for you: <style>.k-textbox-container:not(.k-state-empty).k-label { margin-top: - 10px;
}
</style>

<TelerikTextBox Label=" Lorem ipsum " /> I must note that this can put the label basically outside of the textbox container and so it may start overlapping with things above it. Regards, Marin Bratanov

### Response

**Tim** answered on 13 Jan 2020

Thanks Marin.
