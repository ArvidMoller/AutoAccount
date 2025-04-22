import Image from "next/image";
import styles from "./page.module.css";

export default function Home() {
  return (
    <div className={styles.page}>
      <header className={styles.header}>
        Auto Konteraren
      </header>

      <main className={styles.main}>
        <form className={styles.form}>
          <label className={styles.label}>Supplier</label>
          <input type="text"></input>
          <label className={styles.label}>Amount</label>
          <input type="number"></input>
          <label className={styles.label}>Department</label>
          <input type="text"></input>
          <label className={styles.label}>Cost Center</label>
          <input type="text"></input>
          <label className={styles.label}>Project ID</label>
          <input type="text"></input>
          <label className={styles.label}>Personnel</label>
          <input type="text"></input>
          <label className={styles.label}>Refrence</label>
          <input type="text"></input>
          <label className={styles.label}>Tax Percentage</label>
          <input type="number"></input>
          <label className={styles.label}>City</label>
          <input type="text"></input>
          <label className={styles.label}>Crated at</label>
          <input type="datetime-local"></input>
          <label className={styles.label}>Category</label>
          <input type="text"></input>

          <button  className={styles.button}>Submit</button>
        </form>

        <section>
          <img src="../public/shap_bar.png" alt="Feature Importence Graph"></img>
        </section>
      </main>
    </div>
  );
}
