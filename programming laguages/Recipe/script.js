// Sample recipe data
const recipes = [
    {
      title: "Pancakes",
      ingredients: ["flour", "milk", "egg", "sugar"],
      type: "Breakfast",
    },
    {
      title: "Caesar Salad",
      ingredients: ["lettuce", "croutons", "parmesan", "chicken"],
      type: "Lunch",
    },
    {
      title: "Spaghetti Bolognese",
      ingredients: ["pasta", "beef", "tomato", "garlic"],
      type: "Dinner",
    },
    {
      title: "Fruit Salad",
      ingredients: ["apple", "banana", "orange", "grape"],
      type: "Snack",
    },
    {
      title: "Omelette",
      ingredients: ["egg", "milk", "cheese"],
      type: "Breakfast",
    },
  ];
  
  // DOM Elements
  const ingredientInput = document.getElementById("ingredientInput");
  const recipeTypeFilter = document.getElementById("recipeTypeFilter");
  const searchButton = document.getElementById("searchButton");
  const recipesGrid = document.getElementById("recipesGrid");
  
  // Function to render recipes
  const renderRecipes = (filteredRecipes) => {
    recipesGrid.innerHTML = "";
  
    if (filteredRecipes.length === 0) {
      recipesGrid.innerHTML = "<p>No recipes found!</p>";
      return;
    }
  
    filteredRecipes.forEach((recipe) => {
      const recipeCard = document.createElement("div");
      recipeCard.className = "recipe-card";
      recipeCard.innerHTML = `
        <h3>${recipe.title}</h3>
        <p>Type: ${recipe.type}</p>
        <p>Ingredients: ${recipe.ingredients.join(", ")}</p>
      `;
      recipesGrid.appendChild(recipeCard);
    });
  };
  
  // Function to filter recipes
  const filterRecipes = () => {
    const query = ingredientInput.value.trim().toLowerCase();
    const selectedType = recipeTypeFilter.value;
  
    let filteredRecipes = recipes;
  
    // Filter by ingredients
    if (query) {
      const queryIngredients = query.split(",").map((ingredient) => ingredient.trim());
      filteredRecipes = filteredRecipes.filter((recipe) =>
        queryIngredients.every((ingredient) => recipe.ingredients.includes(ingredient))
      );
    }
  
    // Filter by type
    if (selectedType) {
      filteredRecipes = filteredRecipes.filter((recipe) => recipe.type === selectedType);
    }
  
    renderRecipes(filteredRecipes);
  };
  
  // Event listener for search button
  searchButton.addEventListener("click", filterRecipes);
  