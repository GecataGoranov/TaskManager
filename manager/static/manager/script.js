document.addEventListener("DOMContentLoaded", () => {
    create_category = document.querySelector("#create-category-button")
    create_category.addEventListener("click",() => {
        if(document.querySelector("#add-assignment-category").style.display == "block"){
            document.querySelector("#add-assignment-category").style.display = "none";
            document.querySelector("#add-assignment-category-label").style.display = "none";
            document.querySelector("#create-category").style.display = "block";
            create_category.innerHTML = '<i class="fas fa-plus me-1"></i>Select a category';
        }
        else{
            document.querySelector("#add-assignment-category").style.display = "block";
            document.querySelector("#add-assignment-category-label").style.display = "block";
            document.querySelector("#create-category").style.display = "none";
            create_category.innerHTML = '<i class="fas fa-plus me-1"></i>Create a category';
        }
    })
})
