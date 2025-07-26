# Maxlength of TextArea

## Question

**Eri** asked on 05 Aug 2022

What is the best/easiest way to limit the number of characters and a user can enter into a TextArea? There is no MaxLength property that I have seen.

## Answer

**Dimo** answered on 08 Aug 2022

Hello Eric, That would be the ValueChanged event. It requires you to update the component Value manually on every event trigger, so you will have full control over what is going on. Regards, Dimo
