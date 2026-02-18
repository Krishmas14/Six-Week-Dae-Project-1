const buttons = document.querySelectorAll("button");

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    button.classList.add("pulse");
    setTimeout(() => button.classList.remove("pulse"), 300);
  });
});
