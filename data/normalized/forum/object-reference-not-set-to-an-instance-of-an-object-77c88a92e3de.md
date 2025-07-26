# Object reference not set to an instance of an object

## Question

**Ron** asked on 01 Apr 2021

During rendering I often get this error. Sometimes I am able to find what mistake I made and fix it. But from the stacktrace in the Chrome debugger it is hard to figure out what is going on. I am working on a WASM project. I was wondering if there were any tips on how to debug issues like this?

## Answer

**Marin Bratanov** answered on 05 Apr 2021

Hello Ronald, The best idea I can offer, in case the stack trace and debugging don't help, is to try adding a few Console.WriteLine() calls in the lifecycle methods of your component. This will show you how far you get before seeing the exception so you can narrow down the search. Another approach with a similar effect is to trim down code to do kind of a binary search - if you remove roughly half the code and the error stops manifesting, it was probably something in that half, so you can repeat the process. Regards, Marin Bratanov Progress Telerik
