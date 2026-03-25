const buttons = document.querySelectorAll("button");
const outputPanel = document.querySelector("#js-output");

const totalLanguages = 80;
const averageSeconds = 3;
const communityActive = true;
const projectName = "PlanetReach";

const weeklyChats = 280;
const dailyChats = Math.round(weeklyChats / 7);
const estimatedWeeklyTranslations = totalLanguages * dailyChats;

const hasFastSpeed = averageSeconds <= 4;
const communityReady = communityActive && dailyChats > 10;

let readinessMessage = "In progress";
if (hasFastSpeed && communityReady) {
  readinessMessage = "Ready for pilot launches.";
} else {
  readinessMessage = "Still tuning performance and community scale.";
}

const outputMessage = `${projectName} update: ~${estimatedWeeklyTranslations} translations per week, ` +
  `${dailyChats} chats/day. Status: ${readinessMessage}`;

console.log(outputMessage);

if (outputPanel) {
  outputPanel.textContent = outputMessage;
}

buttons.forEach((button) => {
  button.addEventListener("click", () => {
    button.classList.add("pulse");
    setTimeout(() => button.classList.remove("pulse"), 300);
  });
});
