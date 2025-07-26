# How to hide spin buttons?

## Question

**Jua** asked on 28 Oct 2020

Simply, how to hide spin buttons?

## Answer

**Marin Bratanov** answered on 28 Oct 2020

Hello Juan, You can set the Arrows paremeter to false. You can see it in action in this demo: [https://demos.telerik.com/blazor-ui/numerictextbox/overview](https://demos.telerik.com/blazor-ui/numerictextbox/overview) Regards, Marin Bratanov

### Response

**Juan Angel** answered on 29 Oct 2020

Thanks a lot !!!!

### Response

**Juan Angel** answered on 29 Oct 2020

Any solution for set Arrows="false" by default in whole project ?

### Response

**Marin Bratanov** answered on 29 Oct 2020

Hi Juan, One way would be to wrap the telerik component in your own component and set that property there. That would mean you have to take care of bubbling events, handling validation, forms, and edit contexts, and generic typing. All of these are things we've already done for you in our component(s). So, another approach could be to use CSS to hide the arrows (it is possible that screen readers might still announce them though). <style>.k-numerictextbox.k-select { display: none;
} </style> <TelerikNumericTextBox @bind-Value="@someField" /> @code{
int someField { get; set; }
} Regards, Marin Bratanov

### Response

**Doug** commented on 02 Nov 2022

I just came across this post and I'm using Telerik Blazor 3.6.1 and adding this CSS worked for me. I only post this to potentially help others. I first attempted the EditorTemplate (which was a lot of work for my grid) .k-numerictextbox.k-spinner-increase { display: none;
}.k-numerictextbox.k-spinner-decrease { display: none;
}

### Response

**Hendrik** commented on 23 Mar 2025

If is not enough. The button is still there but without an icon or functionality. You will see that if you try to set the alignment of the textbox to right. You need the following:.k-input-md .k-input-spinner, .k-picker-md .k-input-spinner{ width: 0; }
