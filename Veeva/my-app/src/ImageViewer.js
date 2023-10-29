import React, { useState, useEffect } from "react";
import useWebSocket, { ReadyState } from "react-use-websocket";

// function ImageViewer() {
//   const [images, setImages] = useState({});  // Stores image data
//   const { sendMessage, lastMessage, readyState } = useWebSocket("ws://localhost:6789");

//   useEffect(() => {
//     if (lastMessage !== null) {
//       // Assuming that the first message is always the filename
//       const fileName = lastMessage.data;
//       // Read next message for the image content
//       const nextMsg = new Blob([lastMessage.data], { type: "image/png" });
//       const imageUrl = URL.createObjectURL(nextMsg);
//       setImages(prevImages => ({ ...prevImages, [fileName]: imageUrl }));
//     }
//   }, [lastMessage]);

//   const connectionStatus = {
//     [ReadyState.CONNECTING]: "Connecting",
//     [ReadyState.OPEN]: "Open",
//     [ReadyState.CLOSING]: "Closing",
//     [ReadyState.CLOSED]: "Closed",
//     [ReadyState.UNINSTANTIATED]: "Uninstantiated",
//   }[readyState];

//   return (
//     <div>
//       <p>WebSocket connection status: {connectionStatus}</p>
//       <div style={{ overflowY: "scroll", height: "90vh" }}>
//         {Object.entries(images).map(([name, url]) => (
//           <div key={name}>
//             <h3>{name.split('.')[0]}</h3>
//             <img src={url} alt={name} style={{ maxWidth: "100%" }} />
//           </div>
//         ))}
//       </div>
//     </div>
//   );
// }

// export default ImageViewer;
function ImageViewer() {
    const [images, setImages] = useState({});
    const [lastFileName, setLastFileName] = useState(null);
    const { sendMessage, lastMessage, readyState } = useWebSocket("ws://localhost:6789");
  
    useEffect(() => {
      if (lastMessage !== null) {
        if (lastFileName === null) {
          // This is the filename message
          setLastFileName(lastMessage.data);
        } else {
          // This is the image content message
          const imageUrl = URL.createObjectURL(new Blob([lastMessage.data], { type: "image/png" }));
          setImages(prevImages => ({ ...prevImages, [lastFileName]: imageUrl }));
          
          // Reset lastFileName for the next sequence
          setLastFileName(null);
        }
      }
    }, [lastMessage]);
  
  const connectionStatus = {
    [ReadyState.CONNECTING]: "Connecting",
    [ReadyState.OPEN]: "Open",
    [ReadyState.CLOSING]: "Closing",
    [ReadyState.CLOSED]: "Closed",
    [ReadyState.UNINSTANTIATED]: "Uninstantiated",
  }[readyState];

  return (
    <div>
      <p>WebSocket connection status: {connectionStatus}</p>
      <div style={{ overflowY: "scroll", height: "90vh" }}>
        {Object.entries(images).map(([name, url]) => (
          <div key={name}>
            <h3>{name.split('.')[0]}</h3>
            <img src={url} alt={name} style={{ maxWidth: "100%" }} />
          </div>
        ))}
      </div>
    </div>
  );
}

export default ImageViewer;
  