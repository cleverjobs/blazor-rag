# Http Error 415 when trying to remove an uploaded file

## Question

**Mar** asked on 02 Apr 2020

I get the following error when attempting to remove an uploaded file. I'm using the example code from the Upload Overview Document [https://docs.telerik.com/blazor-ui/components/upload/overview?_ga=2.20672573.407168315.1585784320-1941347284.1557871324](https://docs.telerik.com/blazor-ui/components/upload/overview?_ga=2.20672573.407168315.1585784320-1941347284.1557871324) VS 2019 Output Window. Failed to load resource: the server responded with a status of 415 () [[https://localhost:44326/api/upload/remove]](https://localhost:44326/api/upload/remove]) Microsoft.AspNetCore.Routing.EndpointMiddleware: Information: Executed endpoint 'TestUpload.Controllers.UploadController.Remove (TestUpload)' Microsoft.AspNetCore.Hosting.Diagnostics: Information: Request finished in 69.8482ms 415 application/problem+json; charset=utf-8 Browser Console. telerik-blazor.js:39 POST [https://localhost:44326/api/upload/remove](https://localhost:44326/api/upload/remove) 415 value @telerik-blazor.js:39 value @telerik-blazor.js:39 value @telerik-blazor.js:39 value @telerik-blazor.js:39 value @telerik-blazor.js:39 u @telerik-blazor.js:1 (anonymous) @blazor.server.js:8 beginInvokeJSFromDotNet @blazor.server.js:8 (anonymous) @blazor.server.js:1 e.invokeClientMethod @blazor.server.js:1 e.processIncomingData @blazor.server.js:1 connection.onreceive @blazor.server.js:1 i.onmessage @blazor.server.js:1

## Answer

**Mark Stevens** answered on 02 Apr 2020

I added the [FromForm] attribute to the Remove method of the API and it's working now. public ActionResult Remove([FromForm] string[] files)

### Response

**Marin Bratanov** answered on 03 Apr 2020

Thank you for sharing your solution with the community, Mark. I have marked it as the answer to this thread. It is a bit odd that the docs wouldn't work immediately, but there can be many specifics around the API endpoints an app can have and the Remove request is, ultimately, a form field in the POST query that contains a string. Regards, Marin Bratanov
