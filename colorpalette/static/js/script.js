const imageUpload = document.querySelector(".image-upload");
const imageInput = document.querySelector(".image-input");
const imageNameDiv = document.querySelector(".image-name");

imageUpload.addEventListener("change", handleImageUpload);

function handleImageUpload(event) {
  console.log(event.target.files[0]);
    const imageName = event.target.files[0].name;
    imageNameDiv.innerText = imageName;
}
