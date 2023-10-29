// import React, { useEffect, useState } from "react";

// function App() {
//   const [images, setImages] = useState({});

//   useEffect(() => {
//     const ws = new WebSocket("ws://localhost:6789");

//     ws.onmessage = (event) => {
//       try {
//         const reader = new FileReader();
//         reader.readAsDataURL(event.data);
//         reader.onloadend = () => {
//           const base64data = reader.result;                
//           setImages((prevImages) => {
//             // Assuming event.data is a Blob with the image data
//             let newImages = { ...prevImages };
//             newImages[event.data.name] = base64data;
//             return newImages;
//           });
//         };
//       } catch (error) {
//         console.error("Error reading image data:", error);
//       }
//     };

//     return () => {
//       ws.close();
//     };
//   }, []);

//   return (
//     <div>
//       {Object.entries(images).map(([name, src]) => (
//         <div key={name}>
//           <h3>{name}</h3>
//           <img src={src} alt={name} style={{ maxWidth: "100%" }} />
//         </div>
//       ))}
//     </div>
//   );
// }

// export default App;
import React from "react";
import "./App.css";
import ImageViewer from "./ImageViewer";

function App() {
  return (
    <div className="App">
      <ImageViewer />
    </div>
  );
}

export default App;
