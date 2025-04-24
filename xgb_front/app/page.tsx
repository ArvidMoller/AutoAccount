// HTML for the next.js app

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
          <label className={styles.label}><strong>Supplier</strong></label>
          <div className={styles.radioDiv}>
            <label className={styles.label}>Supplier1</label>
            <input className={styles.radioButtons} type="radio" name="supplier"></input>
            <label className={styles.label}>Supplier2</label>
            <input className={styles.radioButtons} type="radio" name="supplier"></input>
            <label className={styles.label}>Supplier3</label>
            <input className={styles.radioButtons} type="radio" name="supplier"></input>
            <label className={styles.label}>Supplier4</label>
            <input className={styles.radioButtons} type="radio" name="supplier"></input>
            <label className={styles.label}>Supplier5</label>
            <input className={styles.radioButtons} type="radio" name="supplier"></input>
          </div>

          <br></br>

          <label className={styles.label}><strong>Amount</strong></label>
          <input type="number"></input>
         
          <br></br>

          <label className={styles.label}><strong>Department</strong></label>
          <div className={styles.radioDiv}>
            <label className={styles.label}>Department1</label>
            <input className={styles.radioButtons} type="radio" name="department"></input>
            <label className={styles.label}>Department2</label>
            <input className={styles.radioButtons} type="radio" name="department"></input>
            <label className={styles.label}>Department3</label>
            <input className={styles.radioButtons} type="radio" name="department"></input>
            <label className={styles.label}>Department4</label>
            <input className={styles.radioButtons} type="radio" name="department"></input>
            <label className={styles.label}>Department5</label>
            <input className={styles.radioButtons} type="radio" name="department"></input>
          </div>

          <br></br>

          <label className={styles.label}><strong>Cost Center</strong></label>
          <div className={styles.radioDiv}>
            <label className={styles.label}>Cost Center1</label>
            <input className={styles.radioButtons} type="radio" name="costcenter"></input>
            <label className={styles.label}>Cost Center2</label>
            <input className={styles.radioButtons} type="radio" name="costcenter"></input>
            <label className={styles.label}>Cost Center3</label>
            <input className={styles.radioButtons} type="radio" name="costcenter"></input>
            <label className={styles.label}>Cost Center4</label>
            <input className={styles.radioButtons} type="radio" name="costcenter"></input>
            <label className={styles.label}>Cost Center5</label>
            <input className={styles.radioButtons} type="radio" name="costcenter"></input>
          </div>

          <br></br>

          <label className={styles.label}><strong>Project ID</strong></label>
          <div className={styles.radioDiv}>
            <label className={styles.label}>ID1</label>
            <input className={styles.radioButtons} type="radio" name="projectid"></input>
            <label className={styles.label}>ID2</label>
            <input className={styles.radioButtons} type="radio" name="projectid"></input>
            <label className={styles.label}>ID3</label>
            <input className={styles.radioButtons} type="radio" name="projectid"></input>
            <label className={styles.label}>ID4</label>
            <input className={styles.radioButtons} type="radio" name="projectid"></input>
            <label className={styles.label}>ID5</label>
            <input className={styles.radioButtons} type="radio" name="projectid"></input>
          </div>

          <br></br>

          <label className={styles.label}><strong>Personnel</strong></label>
          <div className={styles.radioDiv}>
            <label className={styles.label}>EMP1</label>
            <input className={styles.radioButtons} type="radio" name="personnel"></input>
            <label className={styles.label}>EMP2</label>
            <input className={styles.radioButtons} type="radio" name="personnel"></input>
            <label className={styles.label}>EMP3</label>
            <input className={styles.radioButtons} type="radio" name="personnel"></input>
            <label className={styles.label}>EMP4</label>
            <input className={styles.radioButtons} type="radio" name="personnel"></input>
            <label className={styles.label}>EMP5</label>
            <input className={styles.radioButtons} type="radio" name="personnel"></input>
          </div>

          <br></br>
          
          <label className={styles.label}><strong>Reference</strong></label>
          <div className={styles.radioDiv}>
            <label className={styles.label}>REF1</label>
            <input className={styles.radioButtons} type="radio" name="reference"></input>
            <label className={styles.label}>REF2</label>
            <input className={styles.radioButtons} type="radio" name="reference"></input>
            <label className={styles.label}>REF3</label>
            <input className={styles.radioButtons} type="radio" name="reference"></input>
            <label className={styles.label}>REF4</label>
            <input className={styles.radioButtons} type="radio" name="reference"></input>
            <label className={styles.label}>REF5</label>
            <input className={styles.radioButtons} type="radio" name="reference"></input>
          </div>

          <br></br>

          <label className={styles.label}><strong>Tax Percentage</strong></label>
          <input type="number"></input>

          <br></br>

          <label className={styles.label}><strong>City</strong></label>
          <div className={styles.radioDiv}>
            <label className={styles.label}>Gothenburg</label>
            <input className={styles.radioButtons} type="radio" name="city"></input>
            <label className={styles.label}>Malmo</label>
            <input className={styles.radioButtons} type="radio" name="city"></input>
            <label className={styles.label}>Stockholm</label>
            <input className={styles.radioButtons} type="radio" name="city"></input>
            <label className={styles.label}>Uppsala</label>
            <input className={styles.radioButtons} type="radio" name="city"></input>
            <label className={styles.label}>Linkoping</label>
            <input className={styles.radioButtons} type="radio" name="city"></input>
          </div>

          <br></br>

          <label className={styles.label}><strong>Crated at</strong></label>
          <input type="datetime-local"></input>

          <br></br>
          
          <label className={styles.label}><strong>Category</strong></label>
          <div className={styles.radioDiv}>
            <label className={styles.label}>Category1</label>
            <input className={styles.radioButtons} type="radio" name="category"></input>
            <label className={styles.label}>Category2</label>
            <input className={styles.radioButtons} type="radio" name="category"></input>
            <label className={styles.label}>Category3</label>
            <input className={styles.radioButtons} type="radio" name="category"></input>
            <label className={styles.label}>Category4</label>
            <input className={styles.radioButtons} type="radio" name="category"></input>
            <label className={styles.label}>Category5</label>
            <input className={styles.radioButtons} type="radio" name="category"></input>
          </div>

          <br></br>

          <input className={styles.button} type="submit" value="Submit"></input>
        </form>

        <section className={styles.graphContainer}>
          <h2>Prediction</h2>
          <p>Account: </p>

          <h2>Feature Importence</h2>
          <Image className={styles.graph} src="/shap_bar.png" width={600} height={393} alt="Feature Importence Graph"/>   {/* Height to width ratio 1,526408450704225352112676056338:1  */}
          <p className={styles.graphText}>A higher SHAP-value means that feature was more relevant in the making of the prediction.</p>
        </section>
      </main>
    </div>
  );
}
