import React, { useState } from 'react';

function VisionCrawlForm() {
  const [inputValue, setInputValue] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();
    const pythonScriptPath = 'path/to/vision_crawl.py';
    const command = `python ${pythonScriptPath} ${inputValue}`;
    console.log(`Running command: ${command}`);
    exec(command, (error, stdout, stderr) => {
      if (error) {
        console.error(`Error running command: ${error}`);
        return;
      }
      console.log(`Command output: ${stdout}`);
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <label htmlFor="input">Enter a URL:</label>
      <input type="text" id="input" value={inputValue} onChange={(event) => setInputValue(event.target.value)} />
      <button type="submit">Submit</button>
    </form>
  );
}

export default VisionCrawlForm;