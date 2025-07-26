# Adding hover and selected style to the card component

## Question

**Mar** asked on 03 Dec 2021

I want to ask if there are classes for adding hover and selected styles for the Card? Would also like the card to act as one big button.

## Answer

**Dimo** answered on 07 Dec 2021

Hi Martin, It is possible to add a hover style to the Card like this: <TelerikCard Width="300px" Class="hoverable-card"> <CardHeader> <CardTitle> Tourism </CardTitle> </CardHeader> <CardImage Src="[https://docs.telerik.com/blazor-ui/components/card/images/rome.jpg">](https://docs.telerik.com/blazor-ui/components/card/images/rome.jpg">) </CardImage> <CardBody> <CardTitle> Rome </CardTitle> <CardSeparator> </CardSeparator> <CardSubTitle> Capital of Italy </CardSubTitle> </CardBody> <CardFooter> Car Footer </CardFooter> </TelerikCard> <style>.hoverable-card:hover { background: #fcc;
} </style> However, I can't think of a way to achieve the other two requirements - a selected style and click behavior. The Card is designed to be presentation component, not an interaction component in its core essence. Surely, the Card content can hold interaction components inside it - for example, like in the Actions and Data Cards demos. If you want to highlight a Card action or state, I can suggest you to use custom CSS classes that change, depending on user behavior. It is also possible for the custom CSS class of a Card to affect child content inside it. Regards, Dimo

### Response

**Cristian** commented on 26 May 2022

You could try this: <TelerikButton Class="hello"> <TelerikCard> <CardHeader Class="text-center"> <CardTitle> Hello </CardTitle> </CardHeader> <CardImage Src="[https://docs.telerik.com/blazor-ui/components/card/images/rome.jpg">](https://docs.telerik.com/blazor-ui/components/card/images/rome.jpg">) </CardImage> <CardBody> <p> World </p> </CardBody> </TelerikCard> </TelerikButton> <style>.hello { padding: 0px;
} </style>
