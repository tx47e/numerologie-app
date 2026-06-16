const form = document.querySelector("#person-form");
const statusBox = document.querySelector("#status");
const linksBox = document.querySelector("#links");
const logBox = document.querySelector("#log");
const button = form.querySelector("button");

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  button.disabled = true;
  statusBox.textContent = "Se ruleaza calculele si se construieste lucrarea completa...";
  linksBox.innerHTML = "";
  logBox.textContent = "";

  const payload = Object.fromEntries(new FormData(form).entries());

  try {
    const response = await fetch("/generate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(payload),
    });

    const result = await response.json();
    if (!response.ok) {
      throw new Error(result.error || "Generarea a esuat.");
    }

    statusBox.textContent = "Lucrarea a fost generata.";
    linksBox.innerHTML = `
      <a href="${result.markdown_url}" target="_blank" rel="noreferrer">${result.markdown_name}</a>
      <a href="${result.html_url}" target="_blank" rel="noreferrer">${result.html_name}</a>
    `;
    logBox.textContent = result.summary;
  } catch (error) {
    statusBox.textContent = "A aparut o problema la generare.";
    logBox.textContent = error.message;
  } finally {
    button.disabled = false;
  }
});
