document.addEventListener("DOMContentLoaded", () => {
    const articlesPerPage = 4; // Number of articles per page
    let currentPage = 1;
    let articles = []; // Array to hold articles
  
    const articleForm = document.getElementById("articleForm");
    const articlesGrid = document.getElementById("articlesGrid");
    const paginationControls = document.getElementById("paginationControls");
    const prevPageButton = document.getElementById("prevPage");
    const nextPageButton = document.getElementById("nextPage");
    const pageNumbersContainer = document.getElementById("pageNumbers");
  
    // Function to display articles
    const displayArticles = () => {
      articlesGrid.innerHTML = "";
      const startIndex = (currentPage - 1) * articlesPerPage;
      const endIndex = Math.min(startIndex + articlesPerPage, articles.length);
  
      const currentArticles = articles.slice(startIndex, endIndex);
  
      currentArticles.forEach(article => {
        const articleCard = document.createElement("div");
        articleCard.className = "article-card";
        articleCard.innerHTML = `
          <h3>${article.title}</h3>
          <p>${article.description}</p>
          ${article.imageURL ? `<img src="${article.imageURL}" alt="Article Image">` : ""}
        `;
        articlesGrid.appendChild(articleCard);
      });
  
      updatePaginationControls();
    };
  
    // Function to update pagination controls
    const updatePaginationControls = () => {
      const totalPages = Math.ceil(articles.length / articlesPerPage);
  
      prevPageButton.disabled = currentPage === 1;
      nextPageButton.disabled = currentPage === totalPages;
  
      pageNumbersContainer.innerHTML = "";
      for (let i = 1; i <= totalPages; i++) {
        const pageButton = document.createElement("button");
        pageButton.textContent = i;
        pageButton.className = i === currentPage ? "active" : "";
        pageButton.addEventListener("click", () => {
          currentPage = i;
          displayArticles();
        });
        pageNumbersContainer.appendChild(pageButton);
      }
    };
  
    // Event listener for form submission
    articleForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const title = document.getElementById("title").value.trim();
      const description = document.getElementById("description").value.trim();
      const imageURL = document.getElementById("imageURL").value.trim();
  
      if (title && description) {
        articles.push({ title, description, imageURL });
        currentPage = Math.ceil(articles.length / articlesPerPage); // Jump to last page
        displayArticles();
        articleForm.reset();
      } else {
        alert("Title and description are required!");
      }
    });
  
    // Event listeners for pagination buttons
    prevPageButton.addEventListener("click", () => {
      if (currentPage > 1) {
        currentPage--;
        displayArticles();
      }
    });
  
    nextPageButton.addEventListener("click", () => {
      const totalPages = Math.ceil(articles.length / articlesPerPage);
      if (currentPage < totalPages) {
        currentPage++;
        displayArticles();
      }
    });
  });
  