import Image from "next/image";
import styles from "./page.module.css";

export default function Home() {
  return (
    <div className={styles.page}>
      <body>
        <header>
          <h1 className="title">
            Auto Konterarn
          </h1>
        </header>

        <main className="main">
          <input className="input-text" type="text" name="Supplier" size={50}></input>
          <input className="input-text" type="text" name="Supplier" size={50}></input>
          <input className="input-text" type="text" name="Supplier" size={50}></input>
          <input className="input-text" type="text" name="Supplier" size={50}></input>
          <input className="input-text" type="text" name="Supplier" size={50}></input>
          <input className="input-text" type="text" name="Supplier" size={50}></input>
          <input className="input-text" type="text" name="Supplier" size={50}></input>
          <input className="input-text" type="text" name="Supplier" size={50}></input>
          <input className="input-text" type="text" name="Supplier" size={50}></input>
          <input className="input-text" type="text" name="Supplier" size={50}></input>
          <input className="input-text" type="text" name="Supplier" size={50}></input>
        </main>
      </body>
    </div>
  );
}
