document.addEventListener("DOMContentLoaded", () => {
    var create_category = document.querySelector("#create-category-button");
    if(create_category){
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
    }

    var remove_category = document.querySelector("#remove-category-button");
    if(remove_category){
        remove_category.addEventListener("click", () => {
            document.querySelector("#remove-category-form").style.display = "block";
        })
    }

    var category_links = document.querySelectorAll(".category-link");
    if(category_links){
        category_links.forEach(link => {
            link.addEventListener("mouseover", () => {
                link.style.color = "#9E9D99";
            })
            link.addEventListener("mouseout", () => {
                link.style.color = "#9E9DFF";
            })
        })
    }
})
