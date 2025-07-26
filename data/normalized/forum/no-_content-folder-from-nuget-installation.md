# no _content-folder from NuGet installation

## Question

**Hei** asked on 09 Dec 2019

The documentation recommends using the static assets approach and says: "You can add the JS Interop file as a static asset from our package, instead of using a CDN. Static assets ( the _content folder ) are automatically included in the solution by the Nuget package, so all that's needed is then to reference the asset:" There is no _content folder (using ZIP archive with private .nupgk files, version 2.5.0) and no assets. Regards Heiko

## Answer

**Marin Bratanov** answered on 09 Dec 2019

Hello Heiko, The _content folder is expanded by the framework into the local nuget cache, and the project copies it from there. It is only inside the .nupkg file we carry. You can see it there if you unzip it. Regards, Marin Bratanov

### Response

**Heiko** answered on 09 Dec 2019

Thanks, I did not realize that. Maybe you can add a small hint to the documentation? Btw. what about the source code of UI for Blazor? Regards Heiko

### Response

**Marin Bratanov** answered on 09 Dec 2019

Hi Heiko, I added it to the docs. I suspected people using Blazor have come upon this by now, but it will be a good addition. On the source code - in the future it will become available for sure. Regards, Marin Bratanov

### Response

**Heiko** answered on 11 Dec 2019

Hi Marin, well, for me using NuGet is like driving a car: it moves, but I don't know exactly how the motor works. ;-) It's just "I need this package, and this, and this, *KLICK*". Thanks for updating the docs!! Regards Heiko
